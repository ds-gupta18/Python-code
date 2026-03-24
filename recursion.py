"""
Recursion is a process in which a function calls itself till  a condition is not met.
Factorial of n (n!) = n * (n-1) * (n-2) *.....* 2 * 1
                    = n * (n-1)!
                    = n * (n-1) * (n-2)!.......
4! = 4 * 3 * 2 * 1

There are 2 parts of any recursive function :-
1. Base/ terminal condition
2. Recursive condition
"""
from jedi.inference.recursion import recursion_limit


#without factorial
def fact(num):
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1

    return factorial

n = 4
print(f"Factorial of {n} is {fact(n)} ")

# With recursion
def fact_rec(num):
    if num == 1:          #base condition
        return 1
    else:
        factorial = num * fact_rec(num-1)    #recursive condition
        return factorial

print(fact_rec(4))




