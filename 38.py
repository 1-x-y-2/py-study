text = input("请输入:")

select = ""

for t in text:
    d = ord(t)
    select += chr(d + 1)

print(select)


ans = ""

for t in select:
    d = ord(t)
    ans += chr(d - 1)

print(ans)