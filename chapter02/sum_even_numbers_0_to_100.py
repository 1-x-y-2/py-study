# i = 0
# while i < 10:
#     print("人生苦短,我用Python")
#     i += 1
# else:
#     print("循环正常结束")

i = 1
total = 0
while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1
else:
    print("循环正常结束")

print(f"0-100的偶数和为{total}")
