# Python List
li = [14,5,8,8,9]

# 1. Access elements

print(li[2])
print(li[-1:])
print(li[1:4])
print(li[:: -1])

# 2. Adding Elements

# 2.1 Append
li.append(10)
print(li)

# 2.2 Insert
li.insert(2, 15)
print(li)

# 2.3 Extend --> Adds all elements of a list to the end of another list
li2 = [1, 2, 3]
li.extend(li2)
print(li)   

# 3. Removing Elements

#3.1 Remove
li.remove(8)
print(li)

# 3.2 Pop --> Removes element at the specified position
li.pop(2) 
print(li)

# 3.3 replacement
li[1] = 20
print(li)

# 3.4 Clear --> Removes all elements from the list
li.clear()
print(li)

# 4. Copy of a List

li2 = li.copy()
li2.append(10)
print(li2)
print(li) # li remains unchanged because li2 is a copy of li

# 5. Sorting a List

# 5.1 Sort --> Sorts the list in ascending order
li.sort()
print(li)

# 5.2 Sort in descending order
li.sort(reverse=True)
print(li)

# 5.3 Sorted --> Returns a new sorted list without changing the original list
li2 = sorted(li)
print(li2)
print(li) # li remains unchanged

# 6. Reversing a List
li.reverse()    
print(li)

# 7. Length of a List
print(len(li))

# 8. Count of an Element in a List
print(li.count(8))

# 9. concatenation
li3 = li + li2
print(li3)

# 10. function in a list

print(sum(li))
print(max(li))
print(min(li))
print(sorted(li))
print(li.index(8))
print("avg:", sum(li)/len(li))
