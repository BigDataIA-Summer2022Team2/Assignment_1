import boto3
import os
import re
import json
from typing import Union
from pydantic import BaseModel

class csvInfo(BaseModel):
    fileName : str
    width : int
    height : int
    className : str # 飞机种类的 class 为 python 内置关键字 需要转换
    xmin : int
    ymin : int
    xmax : int
    ymax : int
    base64 : str
    RGB : dict
    valid_width : int
    valid_height : int
    fileSize : str
    aircraft_more_than_1 : bool
    aircraft_num : int
    
    
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
    
    # Print out bucket names
    # for bucket in mybuckets.buckets.all():
    #     print(bucket.name)

    csv_list = mybuckets.Bucket('damg7245-amazon-s3').objects.all()
    str='{"name":"lucy","sex":"boy"}'
    json_csv_info=json.loads(str)
    json_csv_info1=json.loads(csv_list)
    return json_csv_info1
    
