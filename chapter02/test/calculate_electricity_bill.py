price = 0.4883
power_usage = float(input("请输入你的用电度数:"))
if power_usage > 4800:
    price = 0.7883
elif power_usage >= 2880:
    price = 0.5383

print(f"电费为{power_usage * price}")
