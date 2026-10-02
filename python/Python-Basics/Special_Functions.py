# SPECIAL FUNCTIONS
# 1. Filter Function.
def is_even(n):
    return n % 2 == 0
result = filter(is_even, [1, 2, 3, 4, 5, 6])
print(list(result)) 

list1 = [15, 45, 35, 100, 50, 96]
div_15 = lambda x: (x%15==0)
res = list(filter(div_15, list1))
print(res)

# 2. Map Function.
li =[1, 2, 3, 4, 5]
square = lambda x: x**2
result = map(square, li)
print(list(result))

# 3. Reduce Function.
from functools import reduce   
a = lambda x, y: x + y
sum = reduce(a, range(1, 11))
print(sum)

# 4. Zip Function.
list1 = [1, 2, 3]   
list2 = ['a', 'b', 'c']
result = zip(list1, list2)
print(list(result))

real_names = ['John', 'Charles', 'Mike']
code_names = ['Alpha', 'Bravo', 'Charlie']
result = zip(real_names, code_names)
print(list(result))

# unzipping values
result = zip(real_names, code_names)
real_names, code_names = zip(*result)
real_names = list(real_names)
code_names = list(code_names)
print(real_names)
print(code_names)


