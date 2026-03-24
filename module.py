"""
.py is a module
types : Built-in and user-defined module

importing a module (syntax) : import module_name
syntax (for importing only few functions/Variables : from module_name import f, f2, f3
syntax to create alias for the imported module : import module_name as alias_name
"""

#Built-in (math, random, date-time....)

import math
# Calculate square root of a number
num =  100
output = math.sqrt(num)  #module.function_name(arg1, arg2...)
print(f"Square root of {num} is {output}")

# Aea of circle:
radius = 5
area_of_circle = math.pi * (radius ** 2)
print(f"Area of circle with radius {radius} is {area_of_circle}")


#Throw a die
from random import randint

value = randint(0, 10)
print(value)


import datetime as dt
t = dt.time(8, 43, 52)
print(t)

d_t = dt.datetime.now()
print(d_t)

