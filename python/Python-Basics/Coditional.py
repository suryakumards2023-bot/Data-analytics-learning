# Conditional Statements in Python
# Conditional statements are used to perform different actions based on different conditions.
# 1.if statement: The if statement is used to test a specific condition. If the condition is true, the block of code inside the if statement is executed.
x = 10
if x > 5:
    print("x is greater than 5")

# 2. if-else statement: The if-else statement is used to test a specific condition. If the condition is true, the block of code inside the if statement is executed. If the condition is false, the block of code inside the else statement is executed.
y = 3   
if y > 5:
    print("y is greater than 5")
else:
    print("y is less than or equal to 5")   
# 3. elif statement: The elif statement is used to test multiple conditions. If the first condition is false, the next condition is tested, and so on. If all conditions are false, the block of code inside the else statement is executed.
z = 7   
if z > 10:
    print("z is greater than 10")
elif z > 5:
    print("z is greater than 5 but not greater than 10")
else:
    print("z is less than or equal to 5")

# 4. Nested if statement: The nested if statement is used to test multiple conditions. If the first condition is true, the block of code inside the if statement is executed. If the first condition is false, the next condition is tested, and so on.
a = 15  
if a > 10:
    if a > 20:
        print("a is greater than 20")
    else:
        print("a is greater than 10 but not greater than 20")

# 5. Ternary operator: The ternary operator is a shorthand way of writing an if-else statement. It is used to assign a value to a variable based on a condition.
b = 5
result = "b is greater than 5" if b > 5 else "b is not greater than 5"
print(result)

# 6. Logical operators: Logical operators are used to combine multiple conditions. The most common logical operators are and, or, and not.
c = 8
if c > 5 and c < 10:
    print("c is greater than 5 and less than 10")

# practice grade calculator
score = 50
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print(f"Your grade is {grade}") 

# practice even or odd number
number = 7  
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number") 

# making a simple calculator using conditional statements
num1 = 10
num2 = 5
operation = "+"     
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
print(f"The result is: {result}")

# practice finding the largest number among three numbers
num1 = 10
num2 = 15
num3 = 8
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print(f"The largest number is: {largest}")