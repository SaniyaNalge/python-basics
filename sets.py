# Set is a collection data type
# It stores unique values only
# Sets are unordered and mutable

#defining a set
my_set = {1, 2, 3, 3, 2}
print(my_set)   # duplicates are removed

# Sets do not support indexing
# We use loops to access elements
numbers = {10, 20, 30}
for num in numbers:
    print(num)

#adding new values to set
fruits = {"apple", "banana"}

fruits.add("mango")          # add one element
fruits.update(["grapes","oranges"])   # add multiple elements

print(fruits)

#remove/delete values from set
fruits.remove("banana")   # removes element (error if not found)
fruits.discard("apple")   # removes element (no error)

fruits.pop()              # removes random element
print(fruits)

#set functions
nums = {1, 2, 3}

print(len(nums))     # number of elements
nums.clear()         # remove all elements
print(nums)

#set operations
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))         # combine sets
print(A.intersection(B))  # common elements
print(A.difference(B))    # elements in A not in B
print(A.symmetric_difference(B))  # elements not common

#in / not-in test or membership test
colors = {"red", "blue", "green"}

print("red" in colors)     # True
print("yellow" in colors)  # False



