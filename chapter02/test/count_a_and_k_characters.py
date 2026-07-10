s = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
cnt_a = 0
cnt_k = 0

for i in s:
    if i == "a":
        cnt_a += 1
    elif i == "k":
        cnt_k += 1

print(cnt_a)
print(cnt_k)
