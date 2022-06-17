import json
import pytest
from _pytest.fixtures import SubRequest

from pathlib import Path
import sys

path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)
from api_functions import getS3BucketBody


# @pytest.mark.parametrize('username,password',[('','xiaoming123434'),('',''),('xiaowang','')])
# def test_ddt(username,password):
#     print(f'{username}--{password}')


# @pytest.mark.parametrize('username,password',[('','xiaoming123434'),('',''),('xiaowang','')])
# def test_ddt1(username,password):
#     assert username == 'xiaowang'
#     print(f'{username}--{password}')



@pytest.mark.parametrize('filename,className',[('4a042db1cef213a1ed865422e6355f76',''),('','F16')])
def test_getAwsS3BucketBody(filename,className):
    json_reponse = {'249': {'filename': '4a042db1cef213a1ed865422e6355f76', 'width': '1600', 'height': '1043', 'class': 'F117', 'xmin': '165', 'ymin': '910', 'xmax': '496', 'ymax': '1013'}, '250': {'filename': '4a042db1cef213a1ed865422e6355f76', 'width': '1600', 'height': '1043', 'class': 'F16', 'xmin': '35', 'ymin': '744', 'xmax': '234', 'ymax': '840'}, '251': {'filename': '4a042db1cef213a1ed865422e6355f76', 'width': '1600', 'height': '1043', 'class': 'F16', 'xmin': '158', 'ymin': '735', 'xmax': '260', 'ymax': '827'}, '252': {'filename': '4a042db1cef213a1ed865422e6355f76', 'width': '1600', 'height': '1043', 'class': 'F16', 'xmin': '376', 'ymin': '735', 'xmax': '625', 'ymax': '825'}, '253': {'filename': '4a042db1cef213a1ed865422e6355f76', 'width': '1600', 'height': '1043', 'class': 'F16', 'xmin': '1325', 'ymin': '744', 'xmax': '1563', 'ymax': '835'}, '254': {'filename': '4a042db1cef213a1ed865422e6355f76', 'width': '1600', 'height': '1043', 'class': 'F117', 'xmin': '616', 'ymin': '59', 'xmax': '751', 'ymax': '110'}}
    
    assert getS3BucketBody.getS3BucketBodyInfo(filename,className)== json_reponse


if __name__=='__main__':
     pytest.main()