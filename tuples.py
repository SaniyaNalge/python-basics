# Tuple is a collection data type
# It stores values of different datatypes in one variable
# Tuples are ordered and immutable (cannot be changed)
#witten in() round bracket and Repetition of values are allowed

# Creating a tuple with different data types
data = (1, "Saniya", 8.5, True)

print(data)

# Indexing starts from 0
colors = ("red", "green", "blue")

print(colors[0])   # first item
print(colors[1])   # second item
print(colors[-1])  # last item

#tuple functions
nums = (4, 2, 8, 1)

print(len(nums))   # total items
print(max(nums))   # largest value
print(min(nums))   # smallest value
print(sum(nums))   # sum of items

colors = ("red", "blue", "green", "blue")
print(colors.count("blue"))   # count occurrences
print(colors.index("blue"))   # first position

# enumerate() is used to get index and value together
# It is mostly used with loops
# Without enumerate()
fruits = ("apple", "banana", "mango")
i = 0
for fruit in fruits:
    print(i, fruit)
    i += 1

# With enumerate() (clean and easy)
for i, fruit in enumerate(fruits):
    print(i, fruit)
