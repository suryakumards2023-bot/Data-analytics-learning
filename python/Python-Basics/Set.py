# python set
# 1. creating a set

s = {1, 2, 3, 4, 5}
print(s)
print(type(s))
print(len(s))

# 2. adding elements to a set

s.add(6)  # Adding a single element
print(s)
s.update([7, 8, 9])  # Adding multiple elements
print(s)

# 3. removing elements from a set

s.remove(9)  # Removing an element (raises KeyError if not found)
print(s)
s.discard(8)  # Removing an element (does not raise an error if not found)
print(s)    
s.pop()  # Removes and returns an arbitrary element
print(s)
s.clear()  # Removes all elements from the set
print(s)

# 4. set operations in set

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print("Set 1:", s1)
print("Set 2:", s2)
print("Union:", s1.union(s2))
print("Intersection:", s1.intersection(s2))
print("Difference:", s1.difference(s2))
print("Symmetric Difference:", s1.symmetric_difference(s2))

# 5. functions in set
# 5.1 isdisjoint() - Returns True if two sets have a null intersection   

print("Is Disjoint:", s1.isdisjoint(s2))
print("Is Disjoint:", s1.isdisjoint({6, 7, 8}))

# 5.2 issubset() - Returns True if all elements of the set are in the other set
print("Is Subset:", s1.issubset(s2))

# 5.3 issuperset() - Returns True if all elements of the other set are in the set
print("Is Superset:", s1.issuperset(s2))