thisdict = dict()
for i in range(10):
    dictAdd = {(i+1, i-1): i/2}
    thisdict.update(dictAdd)
#print(thisdict)
sorted(thisdict.items(),key=lambda thisdict:thisdict[1])
print(thisdict)
