from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message': 'hello world'}

@app.get("/new_page")
def newpage():
    return {'message':'welcome to new page'}