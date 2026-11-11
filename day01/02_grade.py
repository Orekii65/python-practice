grade=int(input('请输入成绩：'))
rate=''
if grade >=90:
    rate='A'
elif grade >=80:
    rate='B'
elif grade >=70:
    rate='C'
elif grade >=60:
    rate='D'
else:
    rate='E'
print(f'等级：{rate}')

