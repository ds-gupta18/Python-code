"""
Create a simple number guessing game.
The user gets 10 chances to guess a number.
If the user guesses thr number before 10 chances, stop asking the number from the user, say congrats and end the game,
if the user never guesses the number, ask them 10 times and then end the game!!
"""
import random
num = 1

print("Welcome to the number guessing game. We have a number that needs to be guessed. You have 10 chance.")
print("The secret number is between 1 and 50.")
secret_number = random.randint(1, 50)
attempts = 10
is_guess_correct = False

while num <= 10:
    print(f"You have {attempts} attempts left")
    number = int(input("Enter your guess: "))
    if number == secret_number:
        print("Congrats! Your guess is correct!")
        is_guess_correct = True
        break
    else:
        if number < secret_number:
            print("You guess is wrong! Try higher.")
        else:
            print("You guess is wrong! Try lower.")
    num += 1
    attempts -= 1

if not is_guess_correct:
    print("Better luck next time!! You exhausted all your attempts.")
print(f"The secret number was {secret_number}. Game Over!")
