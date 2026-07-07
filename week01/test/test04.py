tempStr = input()
if tempStr[0] in ['C']:
    F = eval(tempStr[1:]) * 1.8 + 32
    print("F{:.2f}".format(F))
elif tempStr[0] in ['F']:
    C = (eval(tempStr[1:]) - 32) / 1.8
    print("C{:.2f}".format(C))