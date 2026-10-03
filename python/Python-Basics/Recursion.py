# Recursion in Python

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(5)
print("Factorial of 5 is:", result)

# fabonacci series using recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
result3 = fibonacci(10)
print("Fibonacci of 10 is:", result3)

# In build function in python
list1 = [1, 2, 3, 4, 5]
result4 = sum(list1)
print("Sum of list is:", result4)

max_value = max(list1)
print("Maximum value in list is:", max_value)

min_value = min(list1)
print("Minimum value in list is:", min_value)

sorted_list = sorted(list1)
print("Sorted list is:", sorted_list)

length = len(list1)
print("Length of list is:", length)

import statistics as s
mean_value = s.mean(list1)
print("Mean of list is:", mean_value)

median_value = s.median(list1)
print("Median of list is:", median_value)

mode_value = s.mode(list1)
print("Mode of list is:", mode_value)

import math
sqrt_value = math.sqrt(16)
factorial_value = math.factorial(5)
print("Square root of 16 is:", sqrt_value)
print("Factorial of 5 is:", factorial_value)


