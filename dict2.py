student1 = {'maths':90.5, 'eng': 76.0, 'phy': 89.0}
print(student1)

print(student1['phy']) #fetch marks for 'phy'
#print(student1['chem']) #fetch marks for 'chem'     #ERROR
print(student1.get('phy'))  #'phy' marks using get()
print(student1.get('chem'))  #'chem' marks using get()
print(student1.get('chem', 40.0))

# Another example
emp1 = {'id': 1001, 'name': 'John', 'salary': 10000}
print (emp1.get('phone'))     #print None
print (emp1.get('phone', 654646645))  #print default val
print (emp1.get('id', 654646645))     #print mentioned key

# Membership operator -> in, ot in
print(1001 in emp1)   #False, 1001 is value not key
print('name' in emp1)

sem1_marks = {'maths': 78.5, 'eng': 71.0, 'phy': 86.5}
sem2_marks = {'chem': 81.5, 'bio': 90.5}

#Update()
sem1_marks.update(sem2_marks)
print(sem1_marks)

groceries_1 = {'milk': 60, 'rice': 100, 'biscuits': 20}
groceries_2 =  {'rice': 110, 'bread': 30}
groceries_1.update(groceries_2)
print(groceries_1)

# Pop()
groceries_1.pop('milk')
print(groceries_1)

# Keys can't be duplicated in dictionary
# dict reads from left to right
groceries_3 = {'milk': 60, 'rice': 100, 'biscuits': 20, 'milk': 65}
print(groceries_3)    #{'milk': 65, 'rice': 100, 'biscuits': 20}