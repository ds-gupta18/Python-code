"""
concatenation(+), repetition(*), membership(in/not in)
count, index
min, max, sum
"""

# +
student_detail1 = (1, "Aman")
student_detail2 = (92.0, 89.5, 93, 96.5, 93)
student_details = student_detail1 + student_detail2
print(student_details)

# *
t1 = ("Class 10", 48000)
print(t1 * 3)

#membership
print(92.0 in student_detail2)
print(99.0 in student_detail2)
print(92.0 not in student_detail2)
print(99.0 not in student_detail2)

# count() : tuple.count(elements)
t1 = (10, 4, 1, 9, 0, 3, 1)
print(t1.count(1))

# index() : tuple.count(elements) (gives the index of the val)
print(t1.index(4))
#print(t1.index(40))    #error
print(t1.index(1))

# min
print(f"Smallest number: {min(t1)}")
# max
print(f"Largest number: {max(t1)}")
# sum
print(f"Total: {sum(t1)}")