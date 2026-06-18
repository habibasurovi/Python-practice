#automatic
a=2
b=3.5
print(a+b)
print(type(a+b)) #type conversion from int to float

c="2"
d=3.5
#print(c+d)
#error because string and float cannot be added
a="hello "
b="world"
print(a+b) #string concatenation

#manual(type casting)
a,b= 2, 3.5
print(a+int(b)) #float to int

x="23"
y=45
print(int(x)+y) #string to int

p=int("44")
q=44.5
print(p+int(q)) #float to int

m= "56.78"
n= 23
print(float(m)+n) #string to float

#char string cannot be converted to int or float

a= 3.14
a=str(a) #float to string
print("it is",a)