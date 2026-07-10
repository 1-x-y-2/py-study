list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
list3 = ['W', 'A', 'S', 'D']

list4 = list1 + list2 + list3
new_list = []
for i in list4:
    if i not in new_list:
        new_list.append(i)

new_list.sort()
print(new_list)