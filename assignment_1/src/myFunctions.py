import boto3
import os
import re
import json
import random
import numpy as np
from typing import Union
from pydantic import BaseModel
import base64

# @Description: input basemodel
# @Author: Cheng Wang
# @UpdateDate: 6/7/2022
class csvInfo(BaseModel):
    #description: Union[str, None] = None
    #price: float
    #tax: Union[float, None] = None
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
    

# @Description: get HTML home page
# @Author: Cheng Wang
# @UpdateDate: 6/12/2022
def getHomePage():
    abs_path = os.path.dirname((os.path.abspath(__file__)))
    html_path = abs_path+"\\index.html"

    html_file = open(html_path, 'r', encoding='utf-8')
    response = html_file.read()

    return response


# @Description: show Pandas Profiling csv info json page
# @Author: Cheng Wang
# @UpdateDate: 6/13/2022
def getPandasProfilingJsonOutput():
    current_dir = os.path.dirname((os.path.abspath(__file__)))
    json_path = current_dir+"\\myTest.json"

    f = open(json_path)
    # returns JSON object as a dictionary
    data = json.load(f)
    # Closing file
    f.close()

    response = data
    return response


# @Description: show Pandas Profiling csv info Html page
# @Author: Cheng Wang
# @UpdateDate: 6/15/2022
def getPandasProfilingCsvHtmlOutput():
    abs_path = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
    html_file_path=abs_path + "\\notebooks\\pandas_profiling\\pandasprofilingcsv.html"

    HtmlFile = open(html_file_path, 'r', encoding='utf-8')
    response = HtmlFile.read()


    return response


# @Description: show Pandas Profiling img info Html page
# @Author: Cheng Wang
# @UpdateDate: 6/15/2022
def getPandasProfilingImageHtmlOutput():
    abs_path = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
    html_file_path=abs_path + "\\notebooks\\pandas_profiling\\pandasprofilingimage.html"

    HtmlFile = open(html_file_path, 'r', encoding='utf-8')
    response = HtmlFile.read()


    return response

#Todo modify
# @Description: get csv file info
# @Author: Cheng Wang
# @UpdateDate: 6/13/2022
def getAllInfo():
    # S3 buckets
    mybuckets = boto3.resource(
        service_name='s3',
        region_name='us-east-1',
        aws_access_key_id='AKIAXUUXEPBEC4KILU6U',
        aws_secret_access_key='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'
    )
    
    count = 0
    info_list = {}
    data = json.loads(json.dumps(info_list)) #json
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
        aircraft_no = 'Image NO.' + str_count

        data[aircraft_no] = aircraft_info
        
        if(count == 5):
            break

    response = data
    
    return response

# @Description: Input aircraft class 
# @Author: Cheng Wang
# @UpdateDate: 6/14/2022
def aircraftClassRequest(request):
    # request_body = json.loads(request)
    # data = request_body.get('class')

    #info_list = {}
    #data = json.loads(json.dumps(info_list))
    #count = 0

    # S3 buckets
    mybuckets = boto3.resource(
        service_name='s3',
        region_name='us-east-1',
        aws_access_key_id='AKIAXUUXEPBEC4KILU6U',
        aws_secret_access_key='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'
    )
 
    result = {}
    index_no = 0
    for obj in mybuckets.Bucket('damg7245-amazon-s3').objects.all():

        key = obj.key
        if "csv" not in key:
            continue

        body = obj.get()['Body'].read()
        body_str = body.decode('utf-8')
        
        csv_header_value_list = body_str.split() # split body into 1 list (contain csv headers and values) header=str->  csv_header_value_list[0]        value=string
        
        inner_index_num = csv_header_value_list[0].split(',')   # header 0-7     [3] class
        
        
        for i in range(len(csv_header_value_list)):
            if(i > 0):
                
                        
                header_list = csv_header_value_list[0].split(',') # split key(header) list
                #split_key_list=csv_header_value_list[i-1][j].split(',')
                    
                csv_header_value_list[i] = csv_header_value_list[i].split(',') #  slipt value list ','
                #split_value_list=csv_header_value_list[i][j].split(',')
    
                if(csv_header_value_list[i][3] != request): #? class_name   
                    continue
                else:
                    index_no += 1 #?   +1 record(key+value)
                    result[str(index_no)] = {} #? str(index_no)= outerkey       result[str(index_no)] = outer_value -> {inner_key : inner_value}

                for j in range(len(inner_index_num)): #? 8 elements 
                    result[str((index_no))][header_list[j]] = csv_header_value_list[i][j] # i = 0      |      j = 0 - 7    

    response = result
    return response

# @Description: Input fileName
# @Author: Cheng Wang
# @UpdateDate: 6/14/2022
def aircraftFileNameRequest(request):
    # S3 buckets
    mybuckets = boto3.resource(
        service_name='s3',
        region_name='us-east-1',
        aws_access_key_id='AKIAXUUXEPBEC4KILU6U',
        aws_secret_access_key='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'
    )
 
    result = {}
    
    for obj in mybuckets.Bucket('damg7245-amazon-s3').objects.all():

        key = obj.key
        if "csv" not in key:
            continue

        body = obj.get()['Body'].read()
        body_str = body.decode('utf-8')
        
        csv_header_value_list = body_str.split() # split body into 1 list (contain csv headers and values) header=str->  csv_header_value_list[0]        value=string
        
        inner_index_num = csv_header_value_list[0].split(',')   # header 0-7 [0] file_name
        index_no = 0
        
        for i in range(len(csv_header_value_list)):
            if(i > 0):
                index_no += 1 #?   +1 record(key+value)
                        
                header_list = csv_header_value_list[0].split(',') # split key(header) list
                #split_key_list=csv_header_value_list[i-1][j].split(',')
                    
                csv_header_value_list[i] = csv_header_value_list[i].split(',') #  slipt value list ','
                #split_value_list=csv_header_value_list[i][j].split(',')
    
                if(csv_header_value_list[1][0] != request): #? request_file_name = file_name -> add json info   
                    continue
                else:
                    result[str(index_no)] = {} #? str(index_no)= outerkey       result[str(index_no)] = outer_value -> {inner_key : inner_value}

                for j in range(len(inner_index_num)): #? 8 elements 
                    result[str((index_no))][header_list[j]] = csv_header_value_list[i][j] # i = 0      |      j = 0 - 7    

    response = result
    return response


# @Description: pass random number from 1-200(Total 200 images) and get n+5 images info
# @Author: Cheng Wang
# @UpdateDate: 6/14/2022
def getOneRandomImage():
    rand_num=random.randint(0,200)
     # S3 buckets
    mybuckets = boto3.resource(
        service_name='s3',
        region_name='us-east-1',
        aws_access_key_id='AKIAXUUXEPBEC4KILU6U',
        aws_secret_access_key='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'
    )
    
    result = {}
    obj_index=0
    for obj in mybuckets.Bucket('damg7245-amazon-s3').objects.all():
        key = obj.key
        if "csv" not in key:
            continue
        
        obj_index+=1

        if(obj_index != rand_num):
            continue
        body = obj.get()['Body'].read()
        body_str = body.decode('utf-8')
        
        csv_header_value_list = body_str.split() # split body into 1 list (contain csv headers and values) header=str->  csv_header_value_list[0]        value=string
        
        inner_index_num = csv_header_value_list[0].split(',')   # header 0-7 [0] file_name
        index_no = 0
        
        for i in range(len(csv_header_value_list)):
            if(i > 0):
                index_no += 1 #   +1 record(key+value)                   
                header_list = csv_header_value_list[0].split(',') # split key(header) list    
                csv_header_value_list[i] = csv_header_value_list[i].split(',') #  slipt value list ','  
                result[str(index_no)] = {} # str(index_no)= outerkey       result[str(index_no)] = outer_value -> {inner_key : inner_value
                for j in range(len(inner_index_num)): # 8 elements 
                    result[str((index_no))][header_list[j]] = csv_header_value_list[i][j] # i = 0      |      j = 0 - 7    

    response = result
    return response


#Todo
# @Description: return Top 1 aircrafts num image(s) info
# @Author: Cheng Wang
# @UpdateDate: 6/14/2022
def getTopNAircraftClassRequest():
    pass


#Todo
# @Description: Input img size (width, height) 500,500 -> 0-500 ,  0-500
# @Author: Cheng Wang
# @UpdateDate: 6/14/2022
def imgSizeRangeInfoRequest(request):
    pass

#Todo
# @Description: Input aircraft position range [xmin,xmax,ymin,ymax] 
# @Author: Cheng Wang
# @UpdateDate: 6/14/2022
def imgSizeRangeRequest(request):
    pass

#Todo
# @Description: Heightlight aircraft bounding box like square or rectangle with color yellow or red
# @Author: Cheng Wang
# @UpdateDate: 6/14/2022
def HighlightAircraftBoundingBox(request):
    pass





#Todo
def showRandomImg():
    data1="""
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
                <h1>Military Aircraft Detection version 7</h1>
    """


    rand_num=random.randint(0,200)
     # S3 buckets
    mybuckets = boto3.resource(
        service_name='s3',
        region_name='us-east-1',
        aws_access_key_id='AKIAXUUXEPBEC4KILU6U',
        aws_secret_access_key='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'
    )


    obj_index=0
    for obj in mybuckets.Bucket('damg7245-amazon-s3').objects.all():
        key = obj.key
        if "image" not in key:
            continue
        
        if(obj_index != rand_num):
            obj_index+=1
            continue

        body = obj.get()['Body'].read()
        img_base64_data = base64.b64encode(body)

        img_data = img_base64_data.decode('utf-8')


    html_img= '<img src="data:image/png;base64,' + img_data +'"/>'
    data2="""     
            </body>
        </html>
    """
    response=data1+html_img+data2
    return response







    



    
