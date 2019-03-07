list1 = [[1,2,3],[4,5,6]]
list2 = list1[:]

list2[1][2]=999


print(list1, "id", id(list1))
print(list2, "id", id(list2))