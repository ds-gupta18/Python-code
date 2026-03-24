def even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

result = even_odd(10)
print(result)
# id code doesn't have return, it returns NONE automatically


# returning values
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = even_odd(9)
print(result)

# returning 2 values
def add(num1, num2):
    result = num1 + num2
    return result

val1 = int(input("Enter a number: "))
val2 = int(input("Enter a number: "))

val = add(val1, val2)
print(f"Addition of {val1} and {val2} is {val}")

#returninng multiple values
def arithmetic(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    return add, sub, mult

val1 = int(input("Enter a number: "))
val2 = int(input("Enter a number: "))

res1, res2, res3 = arithmetic(val1, val2)
print(f"Addition of {val1} and {val2} is {res1}")
print(f"Subtraction of {val1} and {val2} is {res2}")
print(f"Multiplication of {val1} and {val2} is {res3}")
