# Python in Tuple

t = (1,5,4,7,6)
print(t)
print(type(t))
print(len(t))

# 1. accessing elements in tuple

s = ("Hello", "World", "Python", "Tuple")
print(s[0])
print(s[:2])
print(s[-1])

# 2. updating elements in tuple
# tuples are immutable, so we cannot update elements directly

t = (1, 2, 3, 4, 5)
# t[0] = 10  # This will raise an error
t1 = (10,) + t[1:]  # Create a new tuple with the updated value
print(t1)

# 3. deleting elements in tuple
# tuples are immutable, so we cannot delete elements directly
# t[0] = 10  # This will raise an error
t1 = t[1:]  # Create a new tuple without the first element
print(t1)

# 4. concatenation of tuples

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2  # Concatenate two tuples
print(t3)

# 5. repetition of tuples
t4 = (1, 2, 3)
t5 = t4 * 3  # Repeat the tuple 3 times
print(t5)

# 6. functions in tuple

t = (1, 2, 3, 4, 5)
print(max(t)) 
print(min(t))
print(sum(t))  
print(sorted(t))
print(t.count(2)) 
print("Avg:", sum(t) / len(t))  

# 7. tuples vs lists (In terms of speed and memory)
# Tuples are faster than lists in terms of execution time
# Tuples use less memory than lists

import time
# Measuring execution time of tuple operations
start = time.time()
t = (1, 2, 3, 4, 5)
for i in range(1000000):
    x = t[2]
end = time.time()
print("Tuple execution time:", end - start)

# Measuring execution time of list operations
start = time.time()
l = [1, 2, 3, 4, 5]
for i in range(1000000):
    x = l[2]
end = time.time()
print("List execution time:", end - start)

# 8. Tuple packing and unpacking
# Tuple packing
t = 1, 2, 3, 4, 5
print(t)

# Tuple unpacking
a, b, c, d, e = t
print(a, b, c, d, e)

# 9. convert tuple to list and vice versa
t = (1, 2, 3, 4, 5)
l = list(t)
print(l)

t1 = tuple(l)
print(t1)   
