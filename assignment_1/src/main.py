from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import myFunctions

app = FastAPI()


@app.post("/csvinfo/{csvInfo}")
async def postCsvInfo(request : myFunctions.csvInfo):
    return request

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

@app.get("/html/", response_class=HTMLResponse)
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
            <h1>Hello!</h1>
        </body>
        </html>
    """