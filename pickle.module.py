import pickle

students = {'student1': {'roll': 101, 'name': 'Alice', 'percent': 92.8},
            'student2': {'roll': 102, 'name': 'Carol', 'percent': 82.6},
            'student3': {'roll': 103, 'name': 'John', 'percent': 72.4}}

print(students)
print(type(students))

#serialization
with open('student.bin', 'bw') as fh:
    for student in students:
        pickle.dump(students[student], fh)

#deserialization
with open('student.bin', 'rb') as fh:
    while True:
        try:
            data = pickle.load(fh)
            print(data, type(data))
        except EOFError:
           print("Done!")
           break



#print the names of the students (list) who got 90 or more percent
student_list_90 = []
with open('student.bin', 'rb') as fh:
    while True:
        try:
            data = pickle.load(fh)
            if data['percent'] >= 90:
                student_list_90.append(data['name'])
        except EOFError:
            print("Done!")
            break
