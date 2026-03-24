# Mutability & Immutability
# List is mutable while string and tuple isn't.

s1 = "Python is fun"
s1.replace("Python","Java")  #not pget printed
print(s1)
s2 = s1.replace("Python","Java")
print(s2)

l1 = ["Mango", "Orange", "Aple"]
l1[-1] = "Apple"
print(l1)
