import boto3
import os
import re
import json
import numpy as np
from typing import Union
from pydantic import BaseModel


class csvInfo(BaseModel):
    fileName : str=None
    width : int=None
    height : int=None
    className : str # 飞机种类的 class 为 python 内置关键字 需要转换
    xmin : int=None
    ymin : int=None
    xmax : int=None
    ymax : int=None
    base64 : str=None
    RGB : dict=None
    valid_width : int=None
    valid_height : int=None
    fileSize : str=None
    aircraft_more_than_1 : bool=None
    aircraft_num : int=None
    
    
    #description: Union[str, None] = None
    #price: float
    #tax: Union[float, None] = None

def getCsvInfo():
    # S3 buckets
    mybuckets = boto3.resource(
        service_name='s3',
        region_name='us-east-1',
        aws_access_key_id='AKIAXUUXEPBEC4KILU6U',
        aws_secret_access_key='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'
    )
    
    count = 0
    info_list = {}
    data = json.loads(json.dumps(info_list))
    # Print out all objs
    for obj in mybuckets.Bucket('damg7245-amazon-s3').objects.all():
        #key = obj.key
        body = obj.get()['Body'].read()

        

        body_str = body.decode('utf-8')
        csv_header_value_list = body_str.split() # split body into 1 list contain csv headers and values
        csv_header_list = csv_header_value_list[0].split(',') # 'filename,width,height,class,xmin,ymin,xmax,ymax'
        
        csv_value_list = csv_header_value_list[1].split(',') # '00b2add164cb42440a52064e390ea3d2,1280,850,B1,322,112,893,618'

        aircraft_info = dict(zip(csv_header_list, csv_value_list))

        count += 1
        str_count = str(count)
        aircraft_no = 'NO.' + str_count

        data[aircraft_no] = aircraft_info
        
        if(count == 5):
            break

    response = data
    
    return response



def aircraft_class_request(request):
    # request_body = json.loads(request)
    # data = request_body.get('class')

    info_list = {}
    data = json.loads(json.dumps(info_list))
    count = 0

    # S3 buckets
    mybuckets = boto3.resource(
        service_name='s3',
        region_name='us-east-1',
        aws_access_key_id='AKIAXUUXEPBEC4KILU6U',
        aws_secret_access_key='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'
    )
 
    for obj in mybuckets.Bucket('damg7245-amazon-s3').objects.all():

        body = obj.get()['Body'].read()

        body_str = body.decode('utf-8')

        csv_header_value_list = body_str.split() # split body into 1 list contain csv headers and values
        
        csv_header_list = csv_header_value_list[0].split(',') # 'filename,width,height,class,xmin,ymin,xmax,ymax'
        
        csv_value_list = csv_header_value_list[1].split(',') # '00b2add164cb42440a52064e390ea3d2,1280,850,B1,322,112,893,618'

        if(csv_value_list[3] == request):
            aircraft_info = dict(zip(csv_header_list,csv_value_list))
            count += 1
            str_count = str(count)
            aircraft_no = 'NO.' + str_count
            data[aircraft_no] = aircraft_info
            
        else:
            continue

        if(count == 10):
            break

    response = data
    return response
    









    # isCSV = re.compile('''(.*?).csv''')
    # match_obj = re.findall(isCSV,key)
    # if match_obj:
    #     pass
    # else:
    #     pass

    
# def aircraft_fileName_request(request):
#     # request_body = json.loads(request)
#     # data = request_body.get('class')

#     info_list = {}
#     data = json.loads(json.dumps(info_list))
#     count = 0

#     # S3 buckets
#     mybuckets = boto3.resource(
#         service_name='s3',
#         region_name='us-east-1',
#         aws_access_key_id='AKIAXUUXEPBEC4KILU6U',
#         aws_secret_access_key='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'
#     )
 
#     for obj in mybuckets.Bucket('damg7245-amazon-s3').objects.all():

#         body = obj.get()['Body'].read() # bytes

#         body_str = body.decode('utf-8') # str

#         csv_header_value_list = body_str.split() # split body into list contain csv headers and values "\n"
        
#         result = {}

#         if(len(csv_header_value_list) > 2):
#             for i in range(0, len(csv_header_value_list)):
#                 for j in range(0, len(csv_header_value_list)):
#                     result[str(i)][j] = 
                    
#         else:
#             csv_header_list = csv_header_value_list[0].split(',') # 'filename,width,height,class,xmin,ymin,xmax,ymax'
        
#             csv_value_list = csv_header_value_list[1].split(',') # '00b2add164cb42440a52064e390ea3d2,1280,850,B1,322,112,893,618'

       



#         if(csv_value_list[0] == request):
#             aircraft_info = dict(zip(csv_header_list,csv_value_list))
#             count += 1
#             str_count = str(count)
#             aircraft_no = 'NO.' + str_count
#             data[aircraft_no] = aircraft_info
#             #break;
#         else:
#             continue

#     response = data
#     return response


    
