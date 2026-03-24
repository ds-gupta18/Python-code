# raise
salary = float(input("Enter salary: "))

if salary < 0:
    raise ValueError("Salary cannot be negative")
else:
    print(f"Your salary is: {salary}")



age = float(input("Enter age: "))

if age < 0:
    raise Exception("age cannot be negative")  #expection covers all type of error
else:
    if age >= 18:
        print("You can vote.")
    else:
        print("You can not vote.")