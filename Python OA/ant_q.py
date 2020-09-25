import random

trail = 0
position_list,direction_list = [],[]


#generate lists
while (len(position_list)<20):
    position_list.append(random.randint(1,120))
    if random.randint(0,1) == 0:
        direction_list.append(-1)
    else:
        direction_list.append(1)
position_list.sort()

# position_list=[8, 12, 25, 35, 44, 51, 58, 59, 65, 75, 77, 81, 86, 87, 91, 92, 102, 106, 107, 108]
# direction_list=[1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1]


#1 to go right
#-1 to go left
def next_position(position_list, direction_list):
        
    for i in range(len(position_list)-1):
        if position_list[i] == position_list[i+1]:
            direction_list[i] = -1
            direction_list[i+1] = 1
        #if next postion are same, stop moving and change direction
        elif position_list[i]+1 == position_list[i+1] and direction_list[i]==1 and direction_list[i+1]==-1:
            direction_list[i] = -1
            direction_list[i+1] = 1 
        #move is next is empty 
        else:
            position_list[i] += direction_list[i]
    position_list[-1] += direction_list[-1]
    

print(position_list,"#left",len(position_list))
print(direction_list,"#left",len(position_list))


#for j in range(0,30):
while(len(position_list)>1):
    #check_direction(position_list,direction_list)
    next_position(position_list,direction_list)
    trail+=1

    print(position_list,"# left",len(position_list),"trail:",trail)
    print(direction_list,"#left",len(position_list),"trail:",trail)

    for i in range(len(position_list)):
        if position_list[0] < 0:
            position_list.pop(0)
            direction_list.pop(0)
        if position_list[-1] > 120:
            position_list.pop()
            direction_list.pop()
        if len(position_list)<1:
            break


print(position_list,"# left",len(position_list))
print(direction_list)
print("number of trail:",trail)
print("number of trail:",trail+min((120-position_list[0]),(position_list[0]))-7)


