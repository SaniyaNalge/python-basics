#printing Hello world
print("hello world!!!")

#checking different datatypes
num=5
num1=5.23
val=True
a="WELCOME"
print(type(num), type(num1), type(val), type(a))

#accepting input from users
name=input("Enter your Name: ")
print(name)
print(type(name))
#accepting integer input
age=int(input("Enter your age: "))
print(age)
print(type(age))

#type-casting
#1.str to int
a = '2'
b = '3'
print('Addition = ', a+b)       #o/p is concatenation of strings

a = int(a)
b = int(b)
print('Addition = ', a+b)       #o/p is actual addition

#2.str to bool
n= "True"
print(type(n))
n=bool(n)
print(type(n))

#Additional funcations of datatype
# abs() function --> gives positive number
print(abs(-15))

# round() function rounds off the digits after decimal point
print(round(6.43))
print(round(9.89))

# round() function with precision
print(round(7.45, 1))   # round till 1 decimal place
print(round(9.869, 2))   # round till 2 decimal place