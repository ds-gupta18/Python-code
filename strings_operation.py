s1 = "Python is fun"
print(s1[0])
print(s1[-1])
print(len(s1))

language = "Python"
version = "3.13.4"
print(language + version)
#print("Python" - "P")             #error
print(s1 * 3)

#membership operation (in, not in)
print("Python" in s1)
print("is" in s1)
print("z" in s1)
print("Java" in s1)

print("Python" not in s1)
print("is" not in s1)
print("z" not in s1)
print("Java" not in s1)

#comparision of strings
print("Python" == "Python")
print("Python" == "Python ")  #false due to space in rhs

#removing spaces from a string - strip()
s1 = "Python "
s2 = s1.strip()
print(s2)
print( "Python" == s2)
s3 = "     Python    "
print(s3.strip() == "Python")

#replace()
s4 = "We are learning Python"
print(s4.strip() == "We are learning Python")
print(s4)
print(s4.replace("We are", "I am"))
print(s4)
print(s4.replace("e", "E"))
print(s4.replace("e", "E", 1))