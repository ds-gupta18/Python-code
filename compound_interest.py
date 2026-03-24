"""
Amount = P * (1 + R/100) ** T
CI = Amount - P
"""
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter time: "))
#amount1 = principal * (1 + rate/100) ** time
amount2 = principal * pow((1 + rate/100), time)
print(round(amount2, 2))
ci = amount2 - principal
print("Compound interest is: ", ci)
print("Compound interest is: ", round(ci))