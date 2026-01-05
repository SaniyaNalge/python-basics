"""Dictionaries are used to store data in key:value pairs.
Keys are unique and values can be changed
A dictionary is a collection which is ordered, and does not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values seperated with commas"""

#defining a dictionary
student = {
    "name": "Saniya",
    "age": 20,
    "branch": "Computer Engineering"
}

print(student)

# Access value using key
print(student["name"])
print(student["branch"])

# Add new key-value pair
student["year"] = "Third Year"

# Update existing value
student["age"] = 21
print(student)

#Dict Functions()
print(student.keys())     # get all keys
print(student.values())   # get all values
print(student.items())    # get key-value pairs
print(student.get("age")) # safe way to get value

student.pop("age")   # remove key 'age'
print(student)

student.clear()      # remove all items
print(student)

# Dictionary inside another dictionary
students = {
    1: {"name": "Saniya", "marks": 85},
    2: {"name": "Riya", "marks": 90}
}

# Access nested values
print(students[1]["name"])
print(students[2]["marks"])


# Loop through key and value
student = {
    "name": "Saniya",
    "age": 20,
    "branch": "CE"
}

for key, value in student.items():
    print(key, ":", value)


