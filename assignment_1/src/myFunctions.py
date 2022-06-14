import boto3
import os
import re
import json
import numpy as np
from typing import Union
import pandas_profiling
from pydantic import BaseModel

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
    

# @Description: HTML home page
# @Author: Cheng Wang
# @UpdateDate: 6/12/2022
def getHomePage():
    abs_path = os.path.dirname((os.path.abspath(__file__)))
    html_path = abs_path+"\\index.html"

    html_file = open(html_path, 'r', encoding='utf-8')
    response = html_file.read()


    return response


# @Description: To show Pandas Profiling json page
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


# @Description: To show Pandas Profiling Html page
# @Author: Cheng Wang
# @UpdateDate: 6/13/2022
def getPandasProfilingHtmlOutput():
    abs_path = os.path.dirname((os.path.abspath(__file__)))
    html_path = abs_path+"\\pandasprofiling.html"

    HtmlFile = open(html_path, 'r', encoding='utf-8')
    response = HtmlFile.read()


    return response


# @Description: To get csv file info
# @Author: Cheng Wang
# @UpdateDate: 6/13/2022
def getAllCsvInfo():
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

# @Description: Input request and output relative img file info(csv)
# @Author: Cheng Wang
# @UpdateDate: 6/12/2022
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
    

def getrandomNumImages():
    pass

def getNumAircraftrsInOneImage():
    pass

def getTopNAircraftClassRequest(request):
    pass


def getTopNAircraftNumRequest(request):
    pass


def HighlightAircraftBoundingBox():
    pass
















    
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


    
