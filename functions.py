# Function is a block of code
# It performs a specific task
# It runs only when it is called

# Function definition
#basic function with (no parameters)
def greet():
    print("Hello, welcome!")

# Function call
greet()

# Function with input values (with parameters)---Positional Parameter passing
def add(a, b):
    print(a + b)

add(5, 3)

#function with return value
# returns a result
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)

#Keyword parameter passing
# Values are passed using parameter names
def subtract(a, b):
    print(a - b)

subtract(b=5, a=10)   # order does not matter

#Default argument parameter passing
# Default value is used if argument is not given
def greet(name="User"):
    print("Hello", name)

greet("Saniya")
greet()

#varialbe lenght arguments
# *args allows passing multiple values
def total(*nums):
    sum = 0
    for n in nums:
        sum += n
    print(sum)

total(10, 20, 30)

#function calling another function
# Function to check even or odd
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Function calling even_odd()
def check_number(num):
    print("Number is", even_odd(num))

check_number(7)

#--------Examples of functions
# Function to manage bank balance
def bank_account(balance, choice, amount=0):
    if choice == "deposit":
        balance += amount
        return balance
    elif choice == "withdraw":
        if amount <= balance:
            balance -= amount
            return balance
        else:
            return "Insufficient balance"
    else:
        return "Invalid option"

print(bank_account(5000, "withdraw", 2000))

# Function to calculate grade based on marks
def calculate_grade(marks):
    if marks >= 90:
        return "Grade A"
    elif marks >= 75:
        return "Grade B"
    elif marks >= 60:
        return "Grade C"
    else:
        return "Fail"

# Calling function
student_marks = 82
print(calculate_grade(student_marks))
