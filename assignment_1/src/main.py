from fastapi import FastAPI, Query, Path
from typing import Union
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from log.logger import logger
import time
import myFunctions
from pydantic import BaseModel

from pathlib import Path
import sys

path = str(Path(Path(__file__).parent.absolute()))
sys.path.insert(0, path)
from api_functions import getS3BucketBody


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/api/allInputInfoRequest/")
async def allInputInfoRequest(filename:str,width:int,height:int,className:str,xmin:int,ymin:int,xmax:int,ymax:int):
    return getS3BucketBody.getS3BucketBodyInfo(filename,width,height,className,xmin,xmax,ymin,ymax)
    
    
@app.get("/api/test/")
async def allInputInfoRequest(filename:Union[str,None]= Query(default="", max_length=32),
                              width:Union[int,None] = Query(default=0),
                              height:Union[int,None] = Query(default=0),
                              className:str = Query(default="", max_length=5),
                              xmin:Union[int,None] = Query(default=0),
                              ymin:Union[int,None] = Query(default=0),
                              xmax:Union[int,None] = Query(default=0),
                              ymax:Union[int,None] = Query(default=0)):
    return getS3BucketBody.getS3BucketBodyInfo(filename,width,height,className,xmin,ymin,xmax,ymax)   
    


@app.get("/api/get/aircraftClassRequest/")
async def aircraftClassRequest(request : str = Query(default="F16",max_length=5)):
    logger.info('=============== API start ===============')
    funcName = getattr(myFunctions.getTopNAircraftClassRequest,'__name__')
    logger.info('Call Interface: {interface}',interface=funcName)
    logger.info( 'Current Time: {tiems}',tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
     
    response = myFunctions.aircraftClassRequest(request)

    logger.info( 'Current Time: {tiems}',tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    logger.info('=============== API end ===============\n\n')
    return response


@app.get("/api/get/fileNameRequest/")
async def fileNameRequest(request : str = Query(default="0cd99a9ee135c7618006540f5b6d9b1b",max_length=32)):
    response = myFunctions.aircraftFileNameRequest(request)
    return response


@app.get('/api/get/allInfo/')
async def getAllImgInfo():
    logger.info('=============== API start ===============')

    funcName = getattr(myFunctions.getAllInfo,'__name__')
    logger.info('Call {interface}  Now Time：{tiems}',interface=funcName, tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    logger.info('=============== API end ===============\n\n')
    
    return myFunctions.getAllInfo()

@app.get("/pandas/html/csv/", response_class=HTMLResponse)
async def getPandasCsvOutputHtmlPage():

    logger.info('=============== API start ===============')

    funcName = getattr(myFunctions.getPandasProfilingCsvHtmlOutput,'__name__')
    logger.info('Interface Name: {interface}\tNow Time: {tiems}',interface=funcName, tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


    response = myFunctions.getPandasProfilingCsvHtmlOutput()


    logger.info('=============== API end ===============\n\n')

    return response


@app.get("/pandas/html/image/", response_class=HTMLResponse)
async def getPandasImageOutputHtmlPage():

    logger.info('=============== API start ===============')

    funcName = getattr(myFunctions.getPandasProfilingImageHtmlOutput,'__name__')
    logger.info('Interface Name: {interface}\tNow Time: {tiems}',interface=funcName, tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


    response = myFunctions.getPandasProfilingImageHtmlOutput()


    logger.info('=============== API end ===============\n\n')

    return response
    

@app.get("/pandas/json/")
async def getPandasJsonPage():

    logger.info('=============== API start ===============')

    funcName = getattr(myFunctions.getPandasProfilingJsonOutput,'__name__')
    logger.info('Interface Name: {interface}\tNow Time: {tiems}',interface=funcName, tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


    response = myFunctions.getPandasProfilingJsonOutput()


    logger.info('=============== API end ===============\n\n')

    return response


@app.get("/", response_class=HTMLResponse)
async def home():
    logger.info('=============== API start ===============')

    funcName = getattr(myFunctions.getHomePage,'__name__')
    logger.info('Interface Name: {interface}\tNow Time: {tiems}',interface=funcName, tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    logger.info('=============== API end ===============\n\n')

    return myFunctions.getHomePage()


@app.get("/image/", response_class=HTMLResponse)
async def displayImage():
    logger.info('=============== API start ===============')

    funcName = getattr(myFunctions.showRandomImg,'__name__')
    logger.info('Interface Name: {interface}\tNow Time: {tiems}',interface=funcName, tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    logger.info('=============== API end ===============\n\n')

    return myFunctions.showRandomImg()



@app.get("/api/get/random/")
async def getOneRandomImage(): 
    
    logger.info('=============== API start ===============')
    funcName = getattr(myFunctions.getOneRandomImage,'__name__')
    logger.info('Call: {interface}',interface=funcName)
    logger.info( 'Process start: {tiems}',tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    response = myFunctions.getOneRandomImage()

    logger.info( 'Process end: {tiems}',tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    logger.info('=============== API end ===============')
    return response



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


############################### DEMO ##################################
# @app.get("/testtttt/")
# async def read_items(aircraft_class: str = Query(default="e.g. F16",max_length=16)):
#     #results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    
#     # test
#     #aircraft_class: int = Path(title="The ID of the item to get"),
#     results = {"aircraft_class": aircraft_class}
#     return results



# @app.get("/testttttttt/{item_id}")
# async def read_items(
#     item_id: int = Path(title="The ID of the item to get"),
#     q: Union[str, None] = Query(default=None, alias="item-query"),
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results


# @app.get('/test/')
# async def root():
#     logger.info('=============== API start ===============')
#     logger.info('URL: 127.0.0.1:/8000/test/')
#     logger.info('HTTP get')
#     # get 请求
#     logger.debug(f"这是日志！")
#     logger.info('这是 {interface} 接口, 当前时间戳为：{tiems}',interface="root", tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
#     logger.error(f"这是一个 error 信息!")
#     logger.warning(f"这是一个 warning 信息!")


#     logger.info('=============== API end ===============\n\n')
#     return {'message':'Hello World!'}


# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

# @app.get("/students/{student_id}")
# async def students_info(student_id: int, str = None):
#     return {"item_id": student_id}


# @app.post("/posts/")
# def post_msg(body:dict):
#     return body