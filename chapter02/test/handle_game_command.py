order = input("请输入你的指令:")
match order:
    case "w" | "W" | "上":
        print("角色向上移动")
    case "s" | "S" | "下":
        print("角色向下移动")
    case "a" | "A" | "左":
        print("角色向左移动")
    case "d" | "D" | "右":
        print("角色向右移动")
    case " " | "跳":
        print("角色跳跃")
    case "j" | "J" | "攻击":
        print("角色发动攻击")
    case "esc" | "ESC" | "退出":
        print("角色退出游戏")
    case _:
        print("无效的指令")
