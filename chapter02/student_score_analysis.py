num = 1, 2, 3, 4, 5

print(num.count(3))
print(num.index(1))
print(type(num))

a = 100
b = 200
c = 300
c, a, b = a, b, c

students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周铁", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)

name_list = [item[1] for item in students]

chinese_grade = [item[2] for item in students]

math_grade = [item[3] for item in students]

english_grade = [item[4] for item in students]

print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")

for stu_id, name, chinese, math, english in students:
    sum_grade = chinese + math + english
    avg = sum_grade / 3
    print(f"{stu_id} \t {name} \t {chinese} \t {math} \t {english} \t {sum_grade} \t {avg:.1f}")

print(f"语文最低分为{min(chinese_grade)}")
print(f"数学最低分为{min(math_grade)}")
print(f"英语最低分为{min(english_grade)}")
print(f"语文最高分为{max(chinese_grade)}")
print(f"数学最高分为{max(math_grade)}")
print(f"英语最高分为{max(english_grade)}")
print(f"语文平均分为{sum(chinese_grade) / len(chinese_grade)}")
print(f"数学平均分为{sum(math_grade) / len(math_grade)}")
print(f"英语平均分为{sum(english_grade) / len(english_grade)}")

print("以下是优秀学生:")
for stu_id, name, *sum_grade in students:
    if sum(sum_grade) / 3 > 90:
        print(name)
