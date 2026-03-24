numbers = [10, 4, -1, 5.5, 7, 1]

#min() - smallest number in the list
print(f"Smallest number: {min(numbers)}")

# max() - largest number in the list
print(f"Largest number: {max(numbers)}")

# sum() - total of the numbers in the lst
print(F"total: {sum(numbers)}")

# Nested list - list inside a list
l1 = [5, 1.5, "Python", True, None, [1,2,3], 10]
print(len(l1))
print(l1[-2])
print(l1[-2][0])

l2 = [[1,2], [3,4], [5,6,[0,1]]]
print(len(l2))
print(l2[2])
print(l2[2][2])
print(l2[2][2][1])