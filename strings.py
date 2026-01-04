#String has to be mentioned within '' or ""
a="Saniya Sandeep Nalge"
print(a)
print(type(a))

# If your string needs ' for some reason, then you can use escape character \ 
#simple use "" around the string
tech='Apple\'s Smartphones'
print(tech)

#to print character at a position in string, pass the index of character
t="Welcome"
print(t[0])
print(t[5])
#concatenating two strings in disrrent ways
#1. using (+)
t1="Hello"
t2="World"
t3=t1+t2
print(t3)
t3=t1+" "+t2
print(t3)
#2. using format function
t3='{} {}'.format(t1 , t2)
print(t3)
#3. using f string
t3 = f'{t1} {t2}'
print(t3)

#funcations of strings
#1. Len() function to find the lenght of string
print(len(t3))
#2. count() function to check how many times a particular character is repeated
print(t3.count('l'))
#3. find() function to check at what index a particular letter exists
#If the passed character does not belong to the string, then it returns -1
print(t3.find('e'))
print(t3.find('x'))
#4. Case sensitive
print(t3.upper())
print(t3.lower())
print(t3.title()) #prints first letter of each word in uppercase and rest in lowercase
#5. Replace() function
print(t3.replace('World','Sir'))
#6. Strip() function removes the blank spaces before and after the first and last character respectively 
s='     Welcome     '
print(s)
print(s.strip())
print(len(s))
print(len(s.strip()))
#7. Split() funtion to break an entire string into list of strins when ',' is used
s1='I am Fine'
print(s1.split(','))