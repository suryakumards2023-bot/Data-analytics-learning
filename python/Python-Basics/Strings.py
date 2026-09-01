# # Python Strings
# # 1. Basic of string 
# s1= "Hello, World!"
# s2 = 'Python is fun!'
# s3= """This is a multi-line string"""
# s4= '"They don\'t argue anymore"'

# print(s1)
# print(s2)
# print(s3)
# print(s4)

# # 2. Formate Techniques
# # 2.1 Using f-string
# name = "deepak"
# age = 30
# message = f"Hello, my name is {name} and I am {age} years old."

# # 2.2 Using format() method
# message2 = "Hello, my name is {} and I am {} years old.".format(name, age)

# # 2.3 Using +
# message3 = "Hello, my name is " + name + " and I am " + str(age) + " years old."

# print(message)
# print(message2)
# print(message3)

# # 3. user input and output
# user_name = input("Enter your name: ")
# age = input("Enter your age: ")  # age is a string input from user
# print(f"Hello, {user_name}! You are {age} years old.")
# print(f"he will be {int(age) + 1} years old next year")
# print(type(age))  # prints the type of age variable

# user_age = int(input("Enter your age: "))  # age is an integer input from user
# print(f"Hello, You are {user_age} years old.")
# print(type(user_age))  # prints the type of user_age variable

# 4. Operations on string    
# 4.1 String concatenation
str1 = "Hello"
str2 = "World"
str3 = str1 + " " + str2
print(str3)

# 4.2 String repetition
str4 = "Python! " * 3
print(str4)

# 4.3 String indexing
str5 = "Python"
print(str5[0])  # prints the first character 
print(str5[5])  # prints the last character 

# 4.4 String slicing
str6 = "Python Programming"
print(str6[0:6])  # prints the first 6 characters
print(str6[7:18])  # prints characters from index 7 to 17
print(str6[7:])  # prints characters from index 7 to the end
print(str6[:6])  # prints characters from the beginning to index 5
print(str6[-11:-1])  # prints characters from index -11 to -2

# 4.5 String methods
str7 = "python programming" 
print(str7.upper())  # converts the string to uppercase
print(str7.lower())  # converts the string to lowercase
print(str7.capitalize())  # capitalizes the first character of the string
print(str7.title())  # capitalizes the first character of each word in the string

# 4.6 String stripping
str8 = "   Hello, World!   "    
print(str8.strip())  # removes whitespace from both ends
print(str8.lstrip())  # removes whitespace from the left end
print(str8.rstrip())  # removes whitespace from the right end

# 4.7 String replacement
str9 = "I love Python programming"  
print(str9.replace("Python", "Java"))  # replaces "Python" with "Java"  

# 4.8 String splitting
str10 = "Python is fun" 
print(str10.split())  # splits the string into a list of words
print(str10.split("is"))  # splits the string into a list of words using "is" as the delimiter

# 4.9 String joining
list1 = ["Python", "is", "fun"]
str11 = " ".join(list1)
print(str11)  # joins the elements of the list into a single string with a space as the delimiter   

# 4.10 String searching
str12 = "Python is fun" 
print(str12.find("is"))  # finds the index of the first occurrence of "is"
print(str12.find("Java"))  # finds the index of the first occurrence of "Java" (returns -1 if not found)
print("is" in str12)  # checks if "is" is a substring of str12
print("Java" in str12)  # checks if "Java" is a substring of str12

# 4.11 String partitioning
str13 = "Python" 
print(str13.partition("th"))  # splits the string into a tuple of three parts: before, the separator, and after

# 4.12 starting and ending with
str14 = "Python"    
print(str14.startswith("Py"))  # checks if the string starts with "Py"
print(str14.endswith("on"))  # checks if the string ends with "on"

# 4.13 maketrans and translate
str15 = "Python"
translation_table = str.maketrans("yth", "Jac") 
print(str15.translate(translation_table))  # translates the string using the translation table

# 4.14 isalpha, isdigit, isspace
str16 = "Python"    
print(str16.isalpha())  # checks if all characters in the string are alphabetic
str17 = "12345"   
print(str17.isdigit())  # checks if all characters in the string are digits
str18 = "   "
print(str18.isspace())  # checks if all characters in the string are whitespace
str19 = "Hello@World"
print(str19.isalnum())  # checks if all characters in the string are alphanumeric