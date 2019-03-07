def addAllNumsBelow(start):
    if start == 0:
        return 0
    else:
        print(start, "loop!!!")
        return start+addAllNumsBelow(start-1)

print(addAllNumsBelow(100))