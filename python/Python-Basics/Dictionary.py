# Python Dictionary

my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)  
print(type(my_dict))

# 1. accessing values

print(my_dict["name"])
print(my_dict.get("age"))
my_dict["age"] = 40
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())


for key, value in my_dict.items():
    print(f"{key}: {value}")

for i in my_dict.keys():
    print(i)
for i in my_dict.values():
    print(i)

# 2. Adding elements    

my_dict["country"] = "USA"
print(my_dict)
my_dict.update({"email": "john@example.com", "phone": "620-456-7890"})
print(my_dict)

# 3. deleting elements
del my_dict["city"]
print(my_dict)
# 3.1 pop()
pop_value = my_dict.pop("age")
print(pop_value)
print(my_dict)
pop_items = my_dict.popitem()
print(my_dict)
# 3.2 clear()
my_dict.clear()
print(my_dict)

# Question

marks = {"Ram":{"physics": 85, "chemistry":95, "math": 99},
        "Shyam":{"physics": 66, "chemistry":65, "math": 79},
        "Mohan":{"physics": 88, "chemistry":96, "math": 65}}
print(marks)

for i,j in marks.items():
    print(f"Name of the Student: {i}")
    for s,m in j.items():
        print(f"{s}:{m}")