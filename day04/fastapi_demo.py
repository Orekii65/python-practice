from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return{"message":"Hello FastAPI"}

@app.get("/students")
def get_students():
    return {
        "code":0,
        "message":"success",
        "data":[{"name":"张三","score":90},
                {"name":"李四","score":92}]
    }
