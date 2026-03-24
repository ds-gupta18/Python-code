import json      #json- java script object notation

# students = {'student1': {'roll': 101, 'name': 'John', 'percent':98.5},
#             'student2': {'roll': 102, 'name': 'Carol', 'percent':92.5},
#             'student3': {'roll': 103, 'name': 'Alice', 'percent':81.5}}
#
# print(students)
# print(type(students))

# #dump()
# with open('students.json', 'w') as fh:
#     #json.dump(students, fh)
#     json.dump(students, fh, indent=4)

students = {'student1': {'roll': 101, 'name': 'John', 'percent':98.5, 'sports': False},
            'student2': {'roll': 102, 'name': 'Carol', 'percent':92.5, 'sports': False},
            'student3': {'roll': 103, 'name': 'Alice', 'percent':81.5, 'sports': True}}

print(students)
print(type(students))

# # #dump() : to  structurize,  dict to JSON
# with open('student_data.json', 'w') as fh:
#     json.dump(students, fh, indent=4)
#
#
# #load() : json to dict
# with open('student_data.json', 'r') as fh:
#    data =  json.load(fh)
#
# print(data)
# print(type(data))

#upadte()
try:
    # read the old data from the JSON file
    with open('student_data.json', 'r') as fh:
       data =  json.load(fh)
except FileNotFoundError:
        with open('student_data.json', 'w') as fh:
            json.dump(students, fh, indent = 4)
else:
    #update operation
    data.update(students)
    # dump() : write the updated data int he jsonn file
    with open('student_data.json', 'w') as fh:
        json.dump(data, fh, indent = 4)




