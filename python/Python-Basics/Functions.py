# Python Functions

# Python parameters/Arguments
# 1. No Parameters

def sum():
    a = 15
    b = 12
    print(a+b)
sum()

def sub():
    a= 14
    b = 2
    return a -b
res = sub()
print(res)

# 2. Single Parameters
def sum(a):
    b = 12
    print(a+b)
sum(5)

def muliple(a):
    b = 10
    return a *b
mul = muliple(2)
print(mul)

# 3. Multiple Parameters
def multiple(a,c,d):
    print(a*c*d)
multiple(1,3,4)

def multiple(a,b,c):
    prod = a*b*c
    return f"{a}x{b}x{c} = {prod}"
res = multiple(2,5,2)
print(res)

# 4. Default Parameters
def myfun(learning = "kapara"):
    return f"I Learn Java From ApanaCollege {learning}"
name = myfun()
print(name)

# 5. Data Structure as a Parameters
def list_items(items):
    for i in items:
        print(i)
fruit = ["apple","graves","orange","mango"]
res = list_items(fruit)
print(res)

# *args and **kwargs
def student(*name,**details):
    print(name)
    print(details)
res = student("Deepak","Prakash",name ="nilesh", age = "255")
print(res)

def fun(*args):
    for i in args:
        print(i)
res = fun(1,5,2,4,8)
print(res)

def myfun(**kwargs):
    print(kwargs)
    for i in kwargs:
        print(i)
res = myfun(name="deepak",age = 25)
print(res)

