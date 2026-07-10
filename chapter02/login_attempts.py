flag = 1
cnt = 0
while flag:
    if cnt == 5:
        print("你不能再操作了")
        break
    cnt += 1
    user_name = input("请输入用户名:")
    password = input("请输入密码:")
    if (user_name == "admin" and password == "666888"
            or user_name == "zhangsan" and password == "123456"
            or user_name == "taoge" and password == "888666"):
        print("登录成功,进入B站首页~")
        flag = 0
    elif user_name == "" or password == "":
        print("用户名和密码不能为空")
    else:
        print("用户名或密码错误,请重新输入!")
