list1 = [[1,3,4],[5,6,7]]
list3 = [x[:] for x in list1]

list3[1][1] = 999

print(list1)
print(list3)

list4 = [1,3,4,5,6,7]
list5 = list4.copy()

list5[1] = 9999999

print(list4)
print(list5)

print(3 in list1)
