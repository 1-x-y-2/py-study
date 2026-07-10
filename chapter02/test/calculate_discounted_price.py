money = float(input("请输入金额:"))
discount = 1
if money >= 500:
    discount = 0.8
elif money >= 300:
    discount = 0.9
elif money >= 100:
    discount = 0.95

print(f"实际应付金额为{money * discount}")
