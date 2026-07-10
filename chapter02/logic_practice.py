grade = int(input("请输入你的成绩:"))

if grade >= 680:
    print("你很不错")

right_account = "18888888888"
right_password = "666888"
account = input("请输入你的账号:")
password = input("请输入你的密码:")
if account == right_account and password == right_password:
    print("登录成功!")
else:
    print("登录失败!")

year = int(input("请输入年份:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("是闰年")
else:
    print("不是闰年")

num = int(input("请输入一个数字:"))
if num > 0:
    print("正数")
elif num < 0:
    print("负数")
else:
    print("零")

user_name = input("请输入用户名:")
password = input("请输入密码:")
if user_name == "admin" and password == "666888":
    print("登录成功!")
elif user_name == "root" and password == "547527":
    print("登录成功!")
elif user_name == "zhangsan" and password == "123456":
    print("登录成功!")
else:
    print("用户名或密码错误")
    print("登录失败!")
