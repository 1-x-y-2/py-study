num_list = [1, 9, 3, 4, 5]

print(type(num_list))

print(num_list[0])
num_list[0] = 2
print(num_list[0])

del num_list[0]
print(num_list[0])

print("-----")
for item in num_list:
    print(item)

nums = [0, 1, 2, 3, 4, 5, 6]
print(nums[::-1])
print(isinstance(nums[:5], list))
print(nums[:-2])

print("---")
nums.append(7)
print(nums)
nums.insert(2, 8)
print(nums)
nums.remove(2)
print(nums)
nums.pop(4)
print(nums)
nums.sort()
print(nums)
nums.reverse()
print(nums)

nums = []
for i in range(10):
    num = int(input(f"请输入第{i + 1}个数字:"))
    nums.append(num)

nums.sort()
print(nums[0])
print(nums[-1])
print(sum(nums) / len(nums))

num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

num_list3 = [*num_list1, *num_list2]

new_list = []
for i in num_list3:
    if i not in new_list:
        new_list.append(i)

print(new_list)

square = [i ** 2 for i in range(1, 21)]

num_list = [19, 23, 54, 64, 87, 20, 109, 232, 123, 43, 26, 55, 72]
res_list = [i ** 2 for i in num_list if i % 2 == 0]

print(square)
print(res_list)
