# Class is a blueprint (design)
# Object is a real instance created from class

# Creating a class without attributes
class Student:
    
    # Method inside class
    def greet(self):
        print("Hello! Welcome to the Student class")

# Creating an object of the class
s1 = Student()

# Calling method using object
s1.greet()


# Creating a class with attributes
class Student:
    # Constructor to initialize data
    def __init__(self, name, roll_no):
        self.name = name        # attribute
        self.roll_no = roll_no  # attribute

    # Method to display student details
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)

# Creating object of Student class
s1 = Student("Saniya", 101)

# Calling method using object
s1.display()

class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

calc = Calculator()
print(calc.add(10, 5))
print(calc.sub(10, 5))

#Bank account
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.balance)

acc = BankAccount(5000)
acc.deposit(2000)
acc.withdraw(1000)
acc.show_balance()
