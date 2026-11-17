import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DATABASE="students_api.db"

app=FastAPI(title="学生管理 API")

class StudentCreate(BaseModel):
    name:str
    score:float
def get_connection():
    conn=sqlite3.connect(DATABASE)
    conn.row_factory=sqlite3.Row
    return conn


def init_db():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        score REAL NOT NULL
    )
    """)    
    conn.commit()
    conn.close()


init_db()

@app.get("/students")
def list_students():
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("SELECT *FROM students ORDER BY id")
    rows=cursor.fetchall()
    
    conn.close()

    students=[dict(row)for row in rows]

    return {

        "code":0,
        "message":"success",
        "data":students
    }
@app.post("/students",status_code=201)
def create_student(student:StudentCreate):
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, score) VALUES (?, ?)",
        (student.name, student.score)
    )


    conn.commit()
    student_id=cursor.lastrowid
    conn.close()

    return{
        "code":0,
        "message":"创建成功",
        "data":{
            "id":student_id,
            "name":student.name,
            "score":student.score
        }

    }

@app.get("/students/{student_id}")
def get_student(student_id:int):
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    )
    row=cursor.fetchone()

    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="学生不存在")

    return {
        "code":0,
        "message":"success",
        "data":dict(row)
    }

@app.put("/students/{student_id}")
def update_student(student_id:int,student:StudentCreate):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET name=?,score=? WHERE id=?",
        (student.name,student.score,student_id)
    )

    conn.commit()

    if cursor.rowcount==0:
        conn.close()
        raise HTTPException(status_code=404,detail="学生不存在")

    conn.close()

    return{
        "code":0,
        "message":"success",
        "data":{
            "id":student_id,
            "name":student.name,
            "score":student.score
        }
    }

@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()

    if cursor.rowcount==0:
        conn.close()
        raise HTTPException(status_code=404,detail="学生不存在")

    conn.close()

    return{
        "code":0,
        "message":"success",
        "data":{
            "id":student_id
        }
    }