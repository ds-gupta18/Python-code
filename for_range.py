#range() - built-in function used to generate sequence of integers in a given interval
# syntax : range(start, stop, step), stop isn't included

# for i in range(start, stop, step):
    # statements

for i in range(1, 11, 1):
    print(i)

# Odd numbers between 1 & 10 (including 1)
for i in range(1, 11, 2):
    print(i)

# Even numbers between 1 and 10
for i in range(2,10,2):
    print(i)

# Reverse order bet 20 & 10 (excluding 10)
for i in range(20,10,-1):
    print(i)

# CountDown from 10 to 1
for i in range(10,0,-1):
    print(i)
print("Happy birthday")

# range(start, stop) ; step is 1 by default
for i in range(1,5):
    print(i)

# range(stop) - 0 to stop-1 with step of 1 & start is o by default
for i in range(5):
    print(i)

groceries = ['salt', 'milk', 'sugar']
for item in groceries:
    print(item)

for index in range(len(groceries)):
    print(index)

profits = [9,11,6,10]
for index in range(len(profits)):
    q = index + 1
    print(f"Profit for quarter {q} is  {profits[index]}")
