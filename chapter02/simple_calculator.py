# day = input("请输入星期(1~7):")
#
# match day:
#     case "1":
#         print("星期一")
#     case "2":
#         print("星期二")
#     case "3":
#         print("星期三")
#     case "4":
#         print("星期四")
#     case "5":
#         print("星期五")
#     case "6":
#         print("星期六")
#     case "7":
#         print("星期天")
#     case _:
#         print("输入有误!")

x = int(input("请输入要运算的第一个数:"))
y = int(input("请输入要运算的第二个数:"))
oper = input("请输入运算符:")

match oper:
    case "+":
        print(f"{x}+{y}={x + y}")
    case "-":
        print(f"{x}-{y}={x - y}")
    case "*":
        print(f"{x}*{y}={x * y}")
    case "/" if y != 0:
        print(f"{x}/{y}={x / y}")
    case _:
        print("运算符异常")
