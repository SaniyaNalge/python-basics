'''Feature	            for loop	                 while loop
Use	                Known iterations	        Unknown iterations
Condition	            Implicit	                Explicit
Initialization	        Automatic	                 Manual
Risk	         Less chance of infinite loop	Infinite loop possible'''

# while loop repeats code
# as long as the condition is True

# Print even numbers from 1 to 10
i = 2

while i <= 10:
    print(i)
    i += 2

# Find sum of numbers from 1 to 10

i = 1
total = 0

while i <= 10:
    total += i
    i += 1

print("Sum is:", total)

#while with break
# Stop loop when i becomes 5

i = 1

while True:
    if i == 5:
        break
    print(i)
    i += 1

#while with continue
# Skip number 3

i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# Find factorial of a number

num = 5
fact = 1

while num > 0:
    fact *= num
    num -= 1

print("Factorial:", fact)

# Menu driven calculator using while loop

while True:
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("Exiting calculator")
        break   # stop the loop

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Result:", a + b)
    elif choice == 2:
        print("Result:", a - b)
    elif choice == 3:
        print("Result:", a * b)
    else:
        print("Invalid choice")

