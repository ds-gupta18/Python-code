"""
>= , grade A
80 & 89, grade B
70 & 79, gradee C
60 & 69, grade D
<60, grade F
"""
marks = float(input("Enter your marks: "))

if marks  >= 90:
    print("Grade A")
elif 80 <= marks < 90:
    print("Grade B")
elif 70 <= marks < 80:
    print("Grade C")
elif marks >= 60 and marks < 70:
    print("Grade D")
else:
    print("Grade F")