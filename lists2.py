#slicing of lists
l1 = [3,4,1,0,4,9,7,3,6]
print(l1[1:6:1])
print(l1[2:7:2])

#concatanation of lists
l2 = [1,7,2]
l3 = [0,5]
print(l2 + l3)
print(l3 + l2)

# repetition of lists
print(l2 * 3)

# append() - adds an item at the end of the list (any datatype)
# syntax : list.append(item)

fruits = ["Mango", "Apple", "Orange"]
print(fruits)
fruits.append("Banana")
print(fruits)

#insert() - adds an element before the specified index
# syntax : list.insert(index, item)

fruits.insert(2,"Guava")
print(fruits)