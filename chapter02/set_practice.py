s1 = {1, 2, 3, 2}
print(s1)
print(type(s1))
s1.add(4)
print(s1)

s1.remove(2)
print(s1)

print(s1.pop())
print(s1)

# s1.clear()
print(s1)

s2 = {5, 6}
print(s1.difference(s2))
print(s1.union(s2))
print(s1.intersection(s2))

football_set = {"王林", "曾牛", "徐立国", "逗天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}

basketball_set = {"张牛", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}

french_set = {"许木", "王卓", "十二", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}

art_set = {"逗天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

print("同时选修了法语和艺术的学生有:")
for name in french_set.intersection(art_set):
    print(name)
print("同时选修了所有四门的学生有:")
for name in french_set.intersection(basketball_set, football_set, art_set):
    print(name)
print("选了足球但没有选篮球的学生有:")
for name in football_set - basketball_set:
    print(name)

stu_set = football_set | basketball_set | french_set | art_set
stu_list = [*football_set, *basketball_set, *french_set, *art_set]
for name in stu_set:
    print(f"{name}选了{stu_list.count(name)}课")
