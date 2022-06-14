from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from log.logger import logger
import os,sys,time
import myFunctions

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")




@app.get("/api/get/aircraftClassRequest/{aircraft_class}")
async def getClassImgInfo(request : str):
    response = myFunctions.aircraftClassRequest(request)
    return response


@app.get("/api/get/fileNameRequest/{aircraft_fileName}")
async def fileNameInfoRequest(request : str):
    response = myFunctions.aircraftFileNameRequest(request)
    return response


@app.get('/api/get/csvInfo/')
async def getCsvFileInfo():
    logger.info('=============== API start ===============')

    funcName = getattr(myFunctions.getAllCsvInfo,'__name__')
    logger.info('这是 {interface} 接口 当前时间戳为：{tiems}',interface=funcName, tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    logger.info('=============== API end ===============\n\n')
    
    return myFunctions.getCsvInfo()

@app.get("/pandas/html/", response_class=HTMLResponse)
async def getPandasHtmlPage():

    logger.info('=============== API start ===============')

    funcName = getattr(myFunctions.getPandasProfilingHtmlOutput,'__name__')
    logger.info('Interface Name: {interface}\tNow Time: {tiems}',interface=funcName, tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


    response = myFunctions.getPandasProfilingHtmlOutput()


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

    response = myFunctions.getHomePage()


    logger.info('=============== API end ===============\n\n')

    return response




############################### DEMO ##################################
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


# # ?Demo
# @app.post("/posts/")
# def post_msg(body:dict):
#     return body