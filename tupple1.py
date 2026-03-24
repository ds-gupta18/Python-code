# Tuple - written in (item1, item2,...); () is optional
# sequence of items as a collection
#immutable

t1 = ("Python", 10, 1.5, True, [1,2,4], (10,20))
print(t1)
print(len(t1))

# Accessing items of a tuple - indexing
print(t1[0])
print(t1[-1])

# () is optional
t2 = (10, 20, 30, 40)
print(t2)
print(type(t2))
t3 = 10, 20, 30, 40
print(t3)
print(type(t3))

#datatype conversion
l1 = [1,2,3]
print(l1, type(l1))
t1 = tuple(l1)
print(t1, type(t1))

fruits = ("apple", "banana", "cherry")
print(fruits, type(fruits))
fruits = list(fruits)
print(fruits, type(fruits))
