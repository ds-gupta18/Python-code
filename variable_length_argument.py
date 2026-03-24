# *args -> variable length positional arguments (0 to n)

def add(*args):
    print(args, type(args))
    return sum(args)

result = add(1,2,3,4,5,6)
print(result)

def add(*nums):              #args is standard
    print(nums, type(nums))
    return sum(nums)

result = add()
print(result)

def student_details(sid, sname, *marks):
    if len(marks) == 0:
        print(f"{sname} with id {sid} was absent in all the exams")
    else:
        percent = sum(marks)/len(marks)
        print(f"{sname} with id {sid} secured {percent}%")

student_details(646, "DS" ,97,89.5,91,82,96.0)
student_details(648, "GK" ,95.5,93,90.0,94,97)
student_details(650, "UN")
