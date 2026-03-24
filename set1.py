# Sets are non-sequential collection of items
# comma separated elements enclosed within {}

set1 = {10, "Python", 2.5}
print(set1)
print(type(set1))

# can't have indexing & slicing with sets
#print(set1[0])   #Error

# Length of the set
print(len(set1))

# no duplicate values (differ than string/tuple)
s1 = {10, 2.5, 10, 30, 10}
print(s1, type(s1))