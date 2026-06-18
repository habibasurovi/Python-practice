#ways to declare string
str= "This is a' string"
str= 'This is a" string'
str= """This is''' a"" string"""

#escape sequence charecters
str= "Hey\nWE are learing \tPython"
print(str)

str1= "Hello "
str2= "World"

#concatenation
str3= str1 + str2
print(str3)
print(str1 + "my" + " " + str2)

#repetition
print(str1 * 3)

 #length of string
len1= len(str1)  
print("Length of 1st string is: ", len1)
print("Length of 2nd string is: ", len(str2))

#indexing
str1= "Hello "
str2= "World"
print(str1[0])  #H
print(str2[4])  #d
#print(str2[6]) #IndexError
print(str1[-1]) #space
print(str2[-2]) #l
#print(str1[-8]) #IndexError

#slicing
str3= "Hello World"
print(str1[1:4]) #ell
print(str2[0:3]) #Wor
print(str2[:3])  #Wor
print(str3[6:]) #World #[6:len(str3)]
print(str3[:])  #Hello World
print(str3[0:5]) #Hello
print(str3[-5:]) #World
print(str3[-5:-2]) #Wor
print(str3[-11:-6]) #Hello
print(str3[-6:-11]) #empty string

