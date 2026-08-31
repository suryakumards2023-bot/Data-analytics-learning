# Python Operators
#  1. Arthimatic Operator  --> +, -, * ,/, %, //, **

a, b = 41, 12
print(a+b)  # Addition
print(a-b)  # Subtraction
print(a*b)  # multiplication
print(a/b)  #Division

x, y = 5, 2
print(x%y)   #Modulus
print(x//y)  #integer Divison
print(x**y)  #Exponent

# 2. Assignment Operators  --> +=, -=, *=, /=

x += y
print(x)
x -= y
print(x)
x *= y
print(x)
x /= y
print(x)

# 3. Comparision Operators --> ==, !=, >, >=, <, <=

p, q = 8, 16
print(p==q)
print(p>q)
print(p<q)
print(p!=q)
print(p<=q)
print(p>=q)

# 4.Logical Operators      --> and, or, not

z = 10
print(z ==2 and z <=5)
print(z ==2 or z <=15)
a = True
print(not a)
val1 = 15
val2 = 25
e = 19
print(e > val1 and val2 > e)
print(e >= val1 or val2 < e)

# 5. Identity Operators    --> is, is not

A = 15
B = 15
print(A is B)
print(A is not B)

# 6. Membership Operators  --> in, not in

l1 = [4,5,6,8,9,2]
print(5 in l1)
print(10 in l1)
print(9 not in l1)




