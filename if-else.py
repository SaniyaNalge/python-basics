# IF statement checks a condition
# If condition is True, code inside IF runs

age = 18

if age >= 18:
    print("You are eligible to vote")

# IF runs when condition is True
# ELSE runs when condition is False

num = -3

if num > 0:
    print("Positive number")
else:
    print("Negative number")

# ELIF checks multiple conditions
# ELSE runs if all conditions are False

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

#Nested If- if inside another If
# Check username and password using nested IF

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Invalid username")


