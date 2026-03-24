import random

# random : returns random float between 0.0 & 1.0 (excluded)
print(random.random())
print(random.random())


# randint(a, b) : returns random int between a & b (both included)
print(random.randint(1, 15))

nums = [10, 4, 1, 8, 4, 3]

# choice(sequence) : returns a random item from the sequence
print(random.choice(nums))

fruits = ["Apple", "Orange", "Mango"]
print(random.choice(fruits))

# shuffle(sequence) : returns the elements shuffled inn random order
random.shuffle(fruits)
print(fruits)