import os
import json
from json import load
from boto3 import client


def getS3BucketBodyInfo(combined_csv):
    bucket=credentials['aws_s3_bucket_name']
    
    #check image or csv
    
    key="csv/" + combined_csv
    abs_path = os.path.dirname((os.path.abspath(__file__)))
    csv_path = abs_path+"\\credentials\\aws_s3_credentials.json"
    credentials = json.load(open(csv_path))
    client = client(service_name=credentials['service_name'],
                 aws_access_key_id=credentials['aws_access_key_id'],
                 aws_secret_access_key=credentials['aws_secret_access_key'])
    
    result = client.get_object(Bucket=bucket, Key=key) 
    body = result["Body"].read().decode()
    return body