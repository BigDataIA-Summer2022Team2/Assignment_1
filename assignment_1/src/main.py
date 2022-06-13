from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import myFunctions
from log.logger import logger
import os,sys,time

app = FastAPI()




@app.post("/post/{aircraft_class}")
async def postCsvInfo(request : str):
    response = myFunctions.aircraft_class_request(request)
    return response


# @app.post("/post/fileName/{aircraft_fileName}")
# async def postCsvInfo(request : str):
#     response = myFunctions.aircraft_fileName_request(request)
#     return response


@app.get('/api/')
async def getCsvFileInfo():
    return myFunctions.getCsvInfo()

# Demo
@app.get("/welcome")
async def hello_world():   
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/students/{student_id}")
async def students_info(student_id: int, str = None):
    return {"item_id": student_id}


@app.post("/posts/")
def post_msg(body:dict):
    return body

@app.get("/", response_class=HTMLResponse)
async def html_page():
    return """
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h1><font color = "#ff6b81">DAMG 7245 Assignment 1</font></h1>
            <h2> <font color="#1e90ff">Team 2 members</font> <h2>
            <h3> <font color="#222f3e">Cheng Wang NUID: 001280107</font><h3>
            <h3> <font color="#222f3e">Meihu Qin NUID: </font><h3><h3>
            <button><a href = "https://github.com/1207Lemon/Big-Data-Systems-Intelligence-Analytics-Labs-Summer-2022"><font color="#8999ef">jump to Github Repo</font></a></button>
            
        </body>
        </html>
    """














# @logger.catch # 异常记录装饰器、放到下面好像不行、应该是异步的关系。
# def my_function(x, y, z):
#     return [x,y,z]


@app.get('/test/')
async def root():
    logger.info('=============== root API start ===============')
    logger.info('URL: 127.0.0.1:/8000/test/')
    logger.info('HTTP get')
    # get 请求
    logger.debug(f"这是日志！")
    logger.info('这是 {interface} 接口, 当前时间戳为：{tiems}',interface="root", tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    logger.error(f"这是一个 error 信息!")
    logger.warning(f"这是一个 warning 信息!")


    logger.info('=============== root API end ===============\n\n')
    return {'message':'Hello World!'}