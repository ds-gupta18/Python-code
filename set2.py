nums = {1, 3, 2, 0, -1}
nums2 = {3, 5}

# Membership operator - in, not in
print(0 in nums)
print(10 in nums)

# concatenation/ repetition - not supported

# Typecasting
week_days = ('Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun')
week_days = set(week_days)
print(week_days)

# Are sets mutable or immutable
set1 = {2, 0, -1}
print(set1)

# add
set1.add(5)
print(set1)
set1.add(0) #trying adding the existing element in set, no difference in output
print(set1)

# Remove
set1.remove(0)
print(set1)
#If we try to remove element not present in a set, it gives error

#discard - used to remove an element, but gives no error while deleting a value not in the set
set1.discard(10)
print(set1)

