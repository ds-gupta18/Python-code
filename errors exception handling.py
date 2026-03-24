"""
1.compile time error : syntax and indentation error
2. Exceptions : errors during execution
"""
## Compile time errors
# 1. syntax error
age = 21
# print(age

# # 2. Indentation error
# if age >= 18:
# print("You can cast vote")


# ##Exceptions:
# #1. Name error
# x = 1000
# result = x + y

# How to handle exceptions : try-except block

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("denominator can't be zero")
except ValueError:
    print("input should only be digits")

