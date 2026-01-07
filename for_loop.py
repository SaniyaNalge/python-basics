# for loop is used to repeat a block of code
# It works with sequences like list, tuple, string, range

for i in range(5):
    print(i)
#prints numbers from 0 to 4

# Print square of numbers from 1 to 5

for i in range(1, 6):
    print(i, "square is", i * i)

# Find sum of numbers from 1 to 10

total = 0

for i in range(1, 11):
    total += i

print("Sum is:", total)

# Print pattern using nested loop

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

# Print table of 5

for i in range(1, 11):
    print("5 x", i, "=", 5 * i)

# Find largest number

nums = [10, 45, 23, 89, 12]
largest = nums[0]

for num in nums:
    if num > largest:
        largest = num

print("Largest number:", largest)


#BREAK statement 
# break stops the loop completely

for i in range(1, 10):
    if i == 5:
        break
    print(i)
#--> Loop stops when i becomes 5

#CONTINUE statement
# continue skips current iteration

for i in range(1, 6):
    if i == 3:
        continue
    print(i)
#--> Skips printing 3

#for loop Ranges
#range(start, stop, step)
# Starts from 0
# Ends at stop-1
# step decides the jump between numbers

# Print even numbers between 1 to 10

for i in range(2, 11, 2):
    print(i)

# Print odd numbers between 1 to 10

for i in range(1, 10, 2):
    print(i)
