

test = [1,2,3,3]

lsum = test[0]
rsum = test[-1]
lp = 0
rp = len(test)-1
#print(rp)




while(lp < rp):
    #print("lp,rp",lp,rp)
    if lsum <= rsum:
        #print(lsum,rsum)
        lp += 1
        lsum += test[lp]
    else:
        #print(lsum,rsum)
        rp -= 1
        rsum += test[rp]

print(lp)






