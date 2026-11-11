students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78}
]
sum=0
for i in range(3):
    print(students[i]['name']+':'+str(students[i]['score']))
    sum+=students[i]['score']
average=sum/len(students)
print(f'平均分：{average:.1f}')
highest=students[0]
for student in students:
    if student['score']>highest['score']:
        highest=student
print('最高分：',highest['name'],highest['score'])

