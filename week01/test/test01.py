tempStr = input()
if tempStr[-1] in ['C', 'c']:
    F = eval(tempStr[0:-1]) * 1.8 + 32
    print("{:.2f}F".format(F))
elif tempStr[-1] in ['F', 'f']:
    C = (eval(tempStr[0:-1]) - 32) / 1.8
    print("{:.2f}C".format(C))
else:
    print("输入格式错误")
