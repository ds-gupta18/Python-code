def func():
    """
    This is a docstring
    We can write what the function does here
    :return: None
    """

    return None

print(help(func))

def divide(num1, num2):
    """
    num1 : A number to be divided   (numerator)
    num2 : A number that divides num1 (denominator)
    :return: float (if num2 isn't 0) or str (if num2 is 0)
    """
    if num2 == 0:
        return "can't divide by zero"
    else:
        result = num1 / num2
        return result

print(divide(10, 4))
print(divide(10, 0))
help(divide)