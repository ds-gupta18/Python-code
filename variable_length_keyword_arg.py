# **kwargs - variable length keyword arguments

def func(**kwargs):
    print(kwargs, type(kwargs))

func(x=10, y=20)
func()

def student_details(sid, sname, *extra, **marks):
    if len(marks) == 0:
        print(f"{sname} did not attend the exam")
    else:
        percent = sum(marks.values())/ len(marks)
        print(f"{sname} with {sid} secured {percent}%")

    print(f"{sname} does {extra}")

student_details(101,"John", 'cricket', sub1=78.5, sub2=81.0, sub3=90.5)
student_details(102,"Karl", 'football', 'debate', sub4=78.5,sub2=88.5,sub1=90.5,sub5=85.5)
student_details(103,"sid")
