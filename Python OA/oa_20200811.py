input=[1,2,-1,4,-1,0]

rls=[]

for i in range(len(input)):
    rls.append([i])

print(rls)

for path in rls:
    root = path[0]
    while(input[root]!= 0 and input[root] not in path):
        path.append(input[root])
        root = input[root]
        print(path)

print(rls)

max = 0
for i in rls:
    if len(i)>max:
        max = len(i)

print(max-1)
