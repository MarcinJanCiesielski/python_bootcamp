import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
number_to_guess = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 10
game_finished = False
if level == "hard":
    attempts = 5

while attempts > 0:
    user_number = int(input("Make a guess: "))
    if number_to_guess == user_number:
        print(f"You WIN.\nI was thinking of number {number_to_guess}")
        game_finished = True
        break
    elif number_to_guess < user_number:
        print("Too high!")
    elif number_to_guess > user_number:
        print("Too low!")
    attempts -= 1
    print(f"Guess again!\nYou have {attempts} attempts remaining to guess the number")

if not game_finished:
    print("You've run out of guesses, you LOSE")
