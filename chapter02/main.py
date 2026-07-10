s = {"a": 1, "b": 2, "c": 3}
print(s)
print(type(s))
print(s["a"])
s["a"] = 9
print(s["a"])
s["d"] = 4
print(s)
print(s.pop("d"))
print(s)
del s["b"]
print(s)
print(s.get("a"))
print("-----")

for key in s.keys():
    print(key)
print("-----")
for value in s.values():
    print(value)
print("-----")
for key, value in s.items():
    print(f"{key}:{value}")

shop = {}
print("欢迎使用购物车管理系统!")
while True:
    oper = input("""请输入你的操作:
    1.添加购物车
    2.修改购物车
    3.删除购物车
    4.查询购物车
    5.退出购物车
    """)
    match oper:
        case "1":
            name = input("请输入商品名称:")
            if name in shop:
                print("商品已经存在!")
            else:
                price = float(input("请输入商品价格."))
                count = int(input("请输入商品数量:"))
                shop[name] = {"price": price, "count": count}
        case "2":
            name = input("请输入要修改的商品名称:")
            if name not in shop:
                print("商品不存在!")
            else:
                shop[name]["price"] = float(input("请输入修改后的商品价格."))
                shop[name]["count"] = int(input("请输入修改后的商品数量:"))
        case "3":
            del shop[input("请输入要删除的商品:")]
        case "4":
            for key, value in shop.items():
                print(f"商品名称: {key}, 商品价格: {value['price']}, 商品数量: {value['count']}")
        case "5":
            print("成功退出!")
            break
        case _:
            print("没有这个选项!")
