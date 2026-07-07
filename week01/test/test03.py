num = input()

template = "零一二三四五六七八九"

for s in num:
    print(template[eval(s)], end='')
