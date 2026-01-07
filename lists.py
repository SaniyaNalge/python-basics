#list stores multiple values in one variable , enclosed in [] square brackets and seperated by ',' commas.
# A list of numbers
numbers = [10, 20, 30, 40]
print(numbers)
# A list of strings
names = ["Saniya", "Amit", "Riya"]
print(names)

#Accessing the string
fruits = ["apple", "banana", "mango"]

print(fruits[0])  # first item
print(fruits[1])  # second item
print(fruits[-1]) # last item
print(fruits[0:2]) #first and second item

#list functions()
numbers = [1, 2, 3]

numbers.append(4)      # add item at end
print(numbers)

numbers.insert(1, 10)  # add at index 1
print(numbers)

numbers.remove(2)      # remove value 2
print(numbers)

numbers.pop()          # remove last item
print(numbers)

#aggregate list functions()
numbers = [5, 2, 9, 1]

print(len(numbers))   # length
print(max(numbers))   # biggest number
print(min(numbers))   # smallest number
print(sum(numbers))   # total sum

#sort and Reverse functions()
nums = [3, 1, 4, 2]
nums.sort()     # sorts numbers
print(nums)
nums.reverse()  # reverses sorted list
print(nums)

fruits = ["apple", "banana", "mango"]
fruits.sort()   # sort list alphabetically
print(fruits)
fruits.reverse()   # reverse list order alphabetically
print(fruits)

#Nested list
marks = [
    [80, 85, 90],   # student 1
    [70, 75, 78],   # student 2
]

print(marks)
print(len(marks))
# Accessing nested items
print(marks[0])      # first student marks
print(marks[0][1])   # second mark of first student



