# Lambda Function
#normal function for square
def square(n):
    return n*n
res = square(5)
print(res)

#lambda function for square
square = lambda n: n*n
res = square(5)
print(res)

#find max of two numbers using normal function
def maximum(a,b):
    if a>b:
        return a
    else:
        return b
res = maximum(10, 20)
print(res)

#find max of two numbers using lambda function
maximum = lambda a, b: a if a > b else b
res = maximum(10, 20)
print(res)

# list of tuples
numbers = [("apple", 2), ("banana", 4), ("cherry", 6)]
numbers.sort(key=lambda x: x[1])
print(numbers)

# list of dictionaries
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 21}
]
students.sort(key=lambda x: x["age"])
print(students)