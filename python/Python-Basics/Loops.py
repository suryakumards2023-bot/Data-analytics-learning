# Python Loops

t = (1, 2, 3, 4, 5)
print(t[0])
print(t[1])

# 1. For Loop --> range(start, stop, step) --> returns a sequence of numbers starting from start (inclusive) to stop (exclusive) with a step value of step. If start is not specified, it defaults to 0. If step is not specified, it defaults to 1.

for i in range(10):
    print(i)

for i in range(1, 10):
    print(i)

for i in range(1, 10, 2):
    print(i)

for i in t:
    print(i)

for i in range(len(t)):
    print(i ,t[i])

# 2. While Loop --> While loops are used to execute a block of code as long as a certain condition is true. The condition is checked before each iteration of the loop.

i = 3
while i < 10:
    print(i)
    i += 1

i = 7
while i > 3:
    print(i)
    i -= 1

# 3. Loop Through a String

name = "programming"
for ch in name:
    print(ch)

# 4.Loop Through a List

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 5. Loop Through a Dictionary

person = { 
    "name": "John",
    "age": 30,
    "city": "New York"
}
for key, value in person.items():
    print(key, value)

# 6. nested Loops --> nested loops are loops that are placed inside another loop. The inner loop is executed for each iteration of the outer loop. Nested loops can be used to iterate over multi-dimensional data structures, such as lists of lists or matrices.

for i in range(2, 5):
    for j in range(5,7):
        print(i, j)

# 7. Break --> is used to exit a loop prematurely when a certain condition is met. When the break statement is encountered, the loop terminates immediately.

for i in range(10):
    if i == 5:
        break
    print(i)

# 8. Continue --> is used to skip the current iteration of a loop and move on to the next iteration. When the continue statement is encountered, the rest of the code inside the loop for that particular iteration is skipped, and the loop proceeds to the next iteration.

for  i in range(10):
    if i == 5:
        continue
    print(i)    

# 9. Pass -- > pass is a null statement in Python. It is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
for i in range(10):
    if i == 5:
        pass
    print(i)   