# 1. Data Types
# Everything in python is an object, so Datatype are  classes and variables instances(objects) these classes
#python has the following Data Types: Integer, Float, Boolean, String, Complex

a = 6
print(type(a))
b = 5.8
print(type(b))
f = False
print(type(f))
s = "Welcome"
print(type(s))
p = 5 + 2j
print(type(p))

# 2. Type Casting  --> Changing the Data type of a varible from one from to another.a

x = 4
print(type(x))

# String to Integer
y = "9"
print(type(y))

y = int(y)
print(type(y))
z = x + y
print(y)

#  Integer to String

age = 20
text = str(age)
print("age:" + text)

# 3. Addition vs Concatenation

a,b = 9,7
print(a+b)
print(type(a+b))

a,b = "9","7"
print(a+b)
print(type(a+b))

a = "deepak"
b = "nilesh"
print(a+b)

x , y = "15", "10"
z = int(x) + int(y)
print(z)
print(type(z))

# Practical Used Cases

math = 85
science = 98
hindi = 95
total = (math + science +hindi)
print("Nilesh score a total of " + (str(total)) + " marks" )

