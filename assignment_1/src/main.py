from fastapi import FastAPI

app = FastAPI()



# Demo

@app.get("/welcome")
async def hello_world():   
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/students/{student_id}")
async def students_info(student_id: int):
    return {"item_id": student_id}

