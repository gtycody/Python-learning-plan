# this file will implete simple I/O

# read file

file = open("Q4_NT.txt", "r")
fileO1 = open("Q4_network.txt", "w")
fileO2 = open("Q4_linksdata.txt", "w")

fileO2.write("0,1,0,99999\n")
fileO2.write("1,0,0,99999\n")

fileO1.write("0,1,0,0,0,0,0\n")

input = file.readlines()


for i in input:
    fileO1.write("0")
    for j in input:
        fileO2.write(str(i[0])+","+
                     str(j[0])+","+
                     str(int(i[2]+i[3])-int(j[2]+j[3]))+","+
                     "99999\n")

        fileO1.write(",1")
    fileO1.write("\n")
