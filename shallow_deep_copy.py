import copy

l1 = [1, 2.5, [10, 20, 30], 'Python']

# # shallow copy  -> only external value changes, internal remains same
# l2 = copy.copy(l1)
# print(l2)
# print(id(l1), id(l2))
# # i.e. l1 & l2 are differ inn their memory location
#
# l1[0] = 100
# print(f"l1 -> {l1}", id(l1))
# print(f"l2 -> {l2}", id(l2))
#
# l1[0] = 5
# l1[2][0] = 50
# print(f"l1 -> {l1}", id(l1))
# print(f"l2 -> {l2}", id(l2))

# deep copy   -> both internal & external value changes
l2 = copy.deepcopy(l1)
l1[0] = 5
l1[2][0] = 50
print(f"l1 -> {l1}", id(l1))
print(f"l2 -> {l2}", id(l2))

