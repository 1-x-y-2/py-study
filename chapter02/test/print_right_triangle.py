n = int(input("请输入直角边的边长:"))
for i in range(n):
    for j in range(i + 1):
        print("*", end="  ")
    print()
