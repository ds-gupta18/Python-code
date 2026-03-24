"""
if marks >= 60, student is pass else fail
and if the student is passed, then we'll print the grade
>= , grade A
80 & 89, grade B
70 & 79, gradee C
60 & 69, grade D
<60, grade F
"""

marks = float(input("Enter your marks: "))

if marks >= 60:
    print("Congrats, you passed the exam")
    if marks >= 90:
        print("Your grade is A")
    elif marks >= 80 and marks < 90:
        print("Your grade is B")
    elif marks >= 70 and marks < 80:
        print("Your grade is C")
    else:
        print("Your grade is D")
else:
    print("You have failed, study hard next time")