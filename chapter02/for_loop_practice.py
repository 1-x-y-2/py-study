# msg = input("请输入要要遍历的字符串:")
# for i in msg:
#     print(i)
# else:
#     print("循环结束")

sum1 = 0
for i in range(1, 101, 2):
    sum1 += i
else:
    print("循环结束")
print(f"1-100之间的奇数和为{sum1}")

sum2 = 0
for i in range(100, 501):
    if i % 3 == 0:
        sum2 += i
else:
    print("循环结束")
print(f"100-500之间所有3的倍数之和为{sum2}")

# m = int(input("请输入m:"))
# n = int(input("请输入n:"))
# for i in range(m):
#     for j in range(n):
#         print("*", end="  ")
#     print()

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j} x {i} = {i * j}", end = "\t")
#     print()


