a = "⬜"
b = "⬛"
for i in range(8):
    a, b = b, a
    for j in range(4):
        print(f"{a}  {b}", end="  ")
    print()
