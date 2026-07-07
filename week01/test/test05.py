money = input()
if money[0] in ['R']:
    u = eval(money[3:]) / 6.78
    print("USD{:.2f}".format(u))
elif money[0] in ['U']:
    r = eval(money[3:]) * 6.78
    print("RMB{:.2f}".format(r))