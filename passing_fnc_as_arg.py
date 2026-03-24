#In python, we can pass a function as an argument of another function

def add_1(number):
    return number + 1
print(add_1(5))

def square(number):
    return number ** 2
print(square(5))



def add1(num):
    return num + 1

def square(num):
    return num ** 2

num = int(input("Enter a num: "))
res1 = add1(num)
res2 = square(res1)
print(f"output is {res2}")

res = square(add1(num))
print(res)