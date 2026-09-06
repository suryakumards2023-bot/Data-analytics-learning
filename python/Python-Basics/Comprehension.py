# Python Comprehension

#1. List Comprehension
# Normal approach
numbers = []
for i in range(1, 6):
    numbers.append(i * 2)
print(numbers)

# Using list comprehension
numbers = [i * 2 for i in range(1, 6)]
print(numbers)
Output: [2, 4, 6, 8, 10]

# With a condition
even = [i for i in range(1, 11) if i % 2 == 0]
print(even)
Output: [2, 4, 6, 8, 10]

# 2. Set Comprehension
numbers = {i * 2 for i in range(1, 6)}
print(numbers)

# 3. Dictionary Comprehension
squares = {i: i * i for i in range(1, 6)}
print(squares)


