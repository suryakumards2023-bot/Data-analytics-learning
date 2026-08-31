# 1. Python Variables 

a = 3
print("Id:",id(a))
b = 3
print("Id:",id(b))
b = 4
print("Id:",id(b))

# 2. Python Keywords

import keyword
print(keyword.kwlist)
print("Total Keywod:",len(keyword.kwlist))

# 3. Declaring Variables

name = "nilesh"
course = "Data Analytic"
print("Nmae:", name)
print("Course:", course)

a = 2
b = 5
c = 6
print(a,b,c)

a,b,c = 2,5,6
print(a,b,c)

# 4. Scope Of Variables

#local scope
def myfun():
    x = 10
    print(x)

myfun()

#global scope
def myfun():
    global x
    x = 8
    print(x)

myfun()
print(x)

# Inside function → local variable gets priority.
# Outside function → global variable is used.
x = 5
def myfun():
    x = 10
    print(x)

myfun()
print(x)

