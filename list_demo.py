'''list is a very strong type in the python'''
strlist = ["a", "b", "c"]
strlist_complex = ["az", "bbz", "ccca", "aaz", "python"]
intlist = [1, 2, 3]
intlist[1] = 4
print(intlist)
print(strlist[1])
print(intlist)
strlist.append("d")
print(strlist)
strlist_copy = strlist.copy()
print(strlist_copy)
print(strlist.index("a"))
strlist.reverse()
print(strlist)
strlist.sort()
print(strlist)
strlist_complex.sort()
print(strlist_complex)
print(strlist_complex.count("aaz"))
print(strlist_complex + strlist)




