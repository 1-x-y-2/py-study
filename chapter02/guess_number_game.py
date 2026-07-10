import random

random_num = random.randint(1, 100)

while True:
    guess_num = int(input("请输入你认为的数字:"))
    if guess_num > random_num:
        print("猜大了")
    elif guess_num < random_num:
        print("猜小了")
    else:
        print("猜对了")
        print("游戏结束")
        break