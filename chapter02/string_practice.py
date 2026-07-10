s = " Hello-Python "
print(s.find("Python"))
print(s.count("Python"))
u_s = s.upper()
print(u_s)
print(u_s.lower())
print(u_s.split("-"))
print(s.strip())
print(s.replace("l", "e"))
print(s.startswith(" "))
print(s.find("A"))

email = input("请输入你的邮箱:")

cnt = email.count("@")

if email.find(".") != -1 and cnt == 1:
    print("邮箱格式正确")
else:
    print("邮箱格式错误")

s = input("请输入一个字符串:")
if s == s[::-1]:
    print("回文")
else:
    print("不回文")

s_list = []
for i in range(10):
    s = input(f"请输入第{i + 1}个字符串:")
    s_list.append(s[::-1].upper())

for item in s_list:
    print(item)