# Creating a set
fruits = {'apple', 'banana', 'orange'}
print(fruits)  # Output: {'banana', 'orange', 'apple'}

# Adding elements to a set
fruits.add('mango')
print(fruits)  # Output: {'banana', 'orange', 'apple', 'mango'}

# Removing elements from a set
fruits.remove('banana')
print(fruits)  # Output: {'orange', 'apple', 'mango'}

# Checking if an element is in a set
print('apple' in fruits)  # Output: True

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union of two sets
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection of two sets
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

# Difference between two sets
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

# Subset and superset
set3 = {1, 2}
print(set3.issubset(set1))  # Output: True
print(set1.issuperset(set3))  # Output: True

# Set comprehension
squares = {x**2 for x in range(1, 6)}
print(squares)  # Output: {1, 4, 9, 16, 25}

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
symmetric_difference_set = set1.symmetric_difference(set2)
