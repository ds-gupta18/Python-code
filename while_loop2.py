num = 10
while num <= 20:
    print(num)
    num += 2

num = 20
while num >= 10:
    print(num)
    num -= 2

correct_password = "Python"

while True:      # infinite loop
    user_password = input("Enter your password: ")
    if user_password == correct_password:
        print("Password is correct! Congrats")
        break
    else:
        print("Password is incorrect, try again!")
print("Logged in!")



