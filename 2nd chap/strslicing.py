#slicing
# string[start : stop : step]
# string[start : stop]

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

str3= "Hello World"
print(str3[::2]) #HloWrd
#Take indices: 0, 2, 4, 6, 8, 10 → H l o W r d

str3= "Hello World"
print(str3[::3]) #Hl r
#Take indices: 0, 3, 6, 9 → H l  r

str3= "Hello World"
print(str3[1::2]) #el ol
#Start at index 1
#Then take every 2nd character
# Indices taken: 1, 3, 5, 7, 9 → e l o l

str3= "Hello World"
print(str3[::-1]) #dlroW olleH
# Start from the end
# Step = -1 means go backwards
# Indices taken: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0
# This simply reverses the string.

str3= "Hello World"
print(str3[::-2]) #dr olH
# Start from the end
# Step = -2 means go backwards by 2
# Indices taken: 10, 8, 6, 4, 2
# → d r   o l H

str3= "Hello World"
print(str3[5::-1]) #olleH
# Start at index 5 (which is a space)
# Go backwards to the beginning
# Indices taken: 5, 4, 3, 2, 1, 0 →   o l l e H

str3= "Hello World"
print(str3[5:0:-1]) #olle
# Start at index 5 (which is a space)
# Go backwards to index 1
# Indices taken: 5, 4, 3, 2, 1 →   o l l e

str3= "Hello World"
print(str3[2:8:2]) #loW
# Start at index 2
# Go to index 8
# Step = 2 means take every 2nd character
# Indices taken: 2, 4, 6 → l o W

str3= "Hello World"
print(str3[8:2:-2]) #Wol
# Start at index 8
# Go to index 2
# Step = -2 means go backwards by 2
# Indices taken: 8, 6, 4 → W o l

str3= "Hello World"
print(str3[:5:-1]) #dlro
# Start at the end
# Go backwards to index 6
# Indices taken: 10, 9, 8, 7, 6 → d l r o W