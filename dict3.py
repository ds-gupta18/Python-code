#d1 = {[1,3,5]: 9,[1,2,1]: 4}
#print(d1)
#d2 = {{1,3,5}: 9,{1,2,1}: 4}
#print(d2)
# d3 = {{'a': 1, 'b': 2}: 6}
# print(d3)
# not allowed key = list, set, dict => mutable
d1 = {"nine": 9, "four": 4}
print(d1)
d2 = {1: True, 0: False}
print(d2)
d3 = {1.0: True, 0.0: False}
print(d3)
d4 = {True: 1, False: 0}
print(d4)
d5 = {(1,3,5): 9,(1,2,1): 4}
print(d5)
# Allowed key = str, int, float,  bool, tuple => immutable
#key of dist can only be mutable datatypes!!

# values can be of any datatype
student1 = {'id': 1001, 'name': 'John', 'marks': [89.5, 71.5, 81.0]}
print(student1)
print(student1['marks'])   #indexing
print(student1['marks'][1])  #chaining

student2 = {'id': 1001, 'name': 'John', 'marks': {'eng': 89.5, 'maths': 71.5, 'bio': 81.0}}
print(student2['marks'])
print(student2['marks']['eng'])

# fetch all the keys
print(student2.keys(), type(student2.keys()))

#fetch all values
print(student2.values(), type(student2.values()))

# items()
print(student2.items()), type(student2.items())