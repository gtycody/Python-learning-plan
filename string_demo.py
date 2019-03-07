'''i will illustrate some basic python String method which is pretty easy'''

str1 = "helloworld"
str2 = " helloworld I love python"
a = "a"

'''string is not immutable both in java and python so do not modify string'''
'''u have to create a new string to do the modification'''
print(str1[0])
print(str1[2:5])
print(str2)
print(str2.strip())
print(len(str1))
'''python will count all the blank as the length of the string'''
print(str1.lower())
print(str1.upper())
'''lower case and upper case switcher'''

'''assignment build a function which could auto turn all the first letter into upper case'''
str1 = " Hello world my name is cody. and i am a student in the university of texas at austin. in this assignment" \
       "i would turn all the start letter in a sentence into upper case"

for i in range(len(str1)):
    if str1[i] == '.':
        print("the", i, "letter is: ", str1[i], " qualified")
        print(str1[i+1].upper())
        str1 = str1[:i+2] + str1[i+2].upper() + str1[i+3:]
        print(str1)
    else:
        print("the", i, "letter is: ", str1[i], " not qualified")
print(str1)



'''in the split method the return type is list'''
str3 = "hello, world"
a = str3.split(",")
print(a)
print(type(a))

