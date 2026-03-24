"""
reverse() -
sort() -
count() -
membership operation
"""
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
nums = [4,9,0,1,2,8]

# reverse
print(days_of_week)
days_of_week.reverse()
print(days_of_week)

# sort()
print(nums)
nums.sort()                #ascending
print(nums)
nums.sort(reverse=True)    #decending
print(nums)

# count() -
num1 = [0, 1, 3, 4, 1, 0, 5, 0, 0, 3, 0]
print(num1)
print(num1.count(0))
print(f"The list is: {num1}")
item_to_count = int(input("Enter the number to be counted from the above list: "))
c = num1.count(item_to_count)
print(f"Occurrences of {item_to_count} in the list is {c}")
language = ["Python", "Java", "C++", "Python"]
print(f"The list is: {language}")
item_to_count = input("Enter the items to be counted from the above list: ")
c = language.count(item_to_count)
print(f"Occurrences of {item_to_count} in the list is {c}")

# membership operation
print("Python" in language)
print("Javascript" in language)
print("Javascript" not in language)
print("Python" not in language)