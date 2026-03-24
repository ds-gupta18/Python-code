"""
extend() - add multiple values ata end of a list
remove() - removes values from a list
pop() - removes one item from the list using index
"""
# extend() --
fruits = ["Apple", "Mango", "Orange"]
print(fruits)
fruits.extend(["Banana", "Grapes"])
print(fruits)
print(len(fruits))
fruits.append(["Banana", "Grapes"])
print(fruits)
print(len(fruits))

# remove() --
fruits.remove("Orange")
print(fruits)
fruits = ["Apple", "Mango", "Orange", "Mango", "Banana", "Grapes"]
print(fruits)
fruits.remove("Mango")
print(fruits)

# pop
fruits.pop(2)
print(fruits)
fruits.pop(-1)
print(fruits)
fruits.pop()
print(fruits)