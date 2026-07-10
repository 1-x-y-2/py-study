# num = 85
#
# num += 10
# print(f"num={num}")
# num -= 10
# print(f"num={num}")
# num *= 10
# print(f"num={num}")
# num /= 10
# print(f"num={num}")
# num //= 10
# print(f"num={num}")
# num %= 3
# print(f"num={num}")
# num **= 3
# print(f"num={num}")


num = int(input("请输入一个整数:"))
print(f"num在10~20之间{num >= 10 and num <= 20}")
print(f"num不在10~20之间{num < 10 or num > 20}")
