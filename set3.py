student1 = {'English', 'Maths', 'CS', 'Physics', 'Chemistry'}
student2 = {'English', 'Biology', 'Physics', 'Chemistry'}
student3 = {'Sanskrit', 'CS'}

print(student1, type(student1))
print(student2, type(student2))

#common subjects of both students - intersection
common_subjects = student1.intersection(student2)
print(common_subjects)   #or
common_subjects = student1 & student2
print(common_subjects)
common_subjects = student1.intersection(student2, student3)
print(common_subjects)

#all subjects of both students - union
all_subjects = student1.union(student2, student3)
print(all_subjects)      #or
all_subjects = student1 | student2 | student3
print(all_subjects)

days = {'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun'}
weekends = {'Sat', 'Sun'}

#difference of sets
weekdays = days - weekends  #name of days, not present in weekends
print(weekdays)   #or
weekdays = days.difference(weekends)
print(weekdays) 