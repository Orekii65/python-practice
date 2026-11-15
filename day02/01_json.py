import json

with open("teststudents.json","r",encoding="utf-8") as f:
    students=json.load(f)
print(students)
with open("teststudents.json","w",encoding="utf-8") as f:
    json.dump(students,f,ensure_ascii=False,indent=2)

print("保存成功")