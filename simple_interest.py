"""
Simple interest = (P * R * T) / 100
P = Principal amount
R = Rate of interest
T = time duration
"""

principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter time: "))
si = (principal * rate * time) / 100
print("Simple interest is: ",si)
