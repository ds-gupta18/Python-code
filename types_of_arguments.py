#Positional arguments -> passing arguments in order of their position
def add(a, b):
    return a + b
result = add(1, 2) # a=1, b=2
print(result)

# Default parameters:
def add(a, b=10): # b is assigned with 10, it'll override any value given to b
    print(f"a: {a}, b: {b}")
    return a + b

result1 = add(3, 4)
print(result1)

result2 = add(8)
print(result2)

# def add(a, b=10, c) - gives error : non-default arguments should not follow the default argument
def sum(a, c, b=10):     #right way
    print(f"a: {a}, b: {b}, c: {c}")
    return a + b + c
result3 = sum(1, 2, 3)
print(result3)
result4 = sum(4, 5)
print(result4)

#Keyword/named arguments
def add(a,b=10,c=20):
    print(f"a: {a}, b: {b}, c: {c}")
    return a + b + c

result5 = add(1, c=10)
print(result5)
result6 = add(c=200,b=80,a=3)
print(result6)
