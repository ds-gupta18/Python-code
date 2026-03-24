#String
s1 = "Hello World"

for char in s1:
    print(char)
print("End of the loop")

# Dictionary
employee = {'empid': 1001, 'name': 'John Gray', 'department': 'HR'}

for i in employee:
    print(i,employee[i])

print(employee.items())

for i in employee.items():       #tupple print
    print(i)

for i in employee.items():          #key print
    print(i[0])

for i in employee.items():          #value print
    print(i[1])

for i in employee.items():          #prints both key & val
    print(i[0], i[1])