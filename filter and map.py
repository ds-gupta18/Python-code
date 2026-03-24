# filter(function, sequence)

seq = [1, 2, 3, 4]

filtered_output = filter(lambda x: True if x % 2 != 0 else False, seq)
print(filtered_output)
print(f"Odd number in the above sequence are: {list(filtered_output)}")

# Map(function, sequence)
seq = [1, 2, 3, 4]

mapped_output = map(lambda x: True if x % 2 != 0 else False, seq)
print(mapped_output)
print(f"map output: {list(mapped_output)}")

seq = [1, 2, 3, 4]

mapped_output = map(lambda x: x ** 2, seq)
print(mapped_output)
print(f"map output: {list(mapped_output)}")
