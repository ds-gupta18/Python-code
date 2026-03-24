#counting substring from a string -- count()
# string.count(substring)

s1 = "We are learning Python. Python is fun."
s2 = "Python"
print(s1.count(s2))
print(f"Occurrences of {s2} is {s1.count(s2)}")
s3 = 'e'
print(f"Occurrences of {s3} is {s1.count(s3)}")
s4 = "learn"
print(f"Occurrences of {s4} is {s1.count(s4)}")
s5 = " "
print(f"Occurrences of space is {s1.count(s5)}")

#Changing case of a string - upper(), lower(), title(), capitalize()
print(s2.upper())
s6 = "We are learning Python 3.13. Python is FUN"
print(s6.upper())
print(s6.lower())
print(s6.title()) #capital of starting letter of each word
print(s6.capitalize()) #Starting letter is capital only

#starting and ending of a string -- startswith(), endswith()
# string.startswith(substring)

s7 = "We are learning Python"
print(s7.startswith("W"))
print(s7.startswith("We"))
print(s7.startswith("w"))
print(s7.startswith("e"))
print(s7.startswith("We are"))

print(s7.endswith("n"))
print(s7.endswith("Python"))
print(s7.endswith("o"))
print(s7.endswith("N"))
print(s7.endswith("on"))

# string iteration
s8 = "Hello"
for char in s8:
    print(char)
