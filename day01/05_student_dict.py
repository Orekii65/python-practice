student = {
    "name": "张三",
    "age": 20,
    "score": 88
}
print(student['name'])
print(student['age'])
print(student['score'])
student['score']='92'
student['city']='南京'
del student['age']
for key,value in student.items():
    print(key,value,sep=':')