import sqlite3

conn=sqlite3.connect("practice.db")
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    score REAL NOT NULL

)
""")

cursor.execute(
    "insert INTO students (name,score) VALUES(?,?)",
    ('张三',96)
)
cursor.execute(
    "insert INTO students (name,score) VALUES(?,?)",
    ('李四',92)
)
cursor.execute(
    "insert INTO students (name,score) VALUES(?,?)",
    ('王五',88)
)

cursor.execute(
    "SELECT * FROM students WHERE score>=80"
)
rows=cursor.fetchall()
print(rows)

cursor.execute(
    "SELECT * FROM students ORDER BY score DESC"
)
rows=cursor.fetchall()
print("降序:",rows)

cursor.execute("SELECT COUNT(*) FROM students")
print("人数：",cursor.fetchone())

cursor.execute("SELECT AVG(score) FROM students")
print("平均分：",cursor.fetchone())

cursor.execute("SELECT MAX(score) FROM students")
print("最高分：",cursor.fetchone())

cursor.execute("UPDATE students SET score =? WHERE name=?",(95,"王五"))

cursor.execute(
    "DELETE FROM students WHERE name = ?",
    ("李四",)
)
conn.commit()

cursor.execute("SELECT * FROM students")
rows=cursor.fetchall()
print(rows)


conn.close()