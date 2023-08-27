import random

from art import logo
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

no_of_attempts = 0

Guess = random.randint(1,100)
if choice == 'easy':
    no_of_attempts = 10
    while no_of_attempts > 0:
        print(f"You have {no_of_attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess == Guess:
            print(f"You got it! The answer was {Guess}.")
            no_of_attempts = -1
        elif user_guess > Guess:
            print("Too High.")
            if no_of_attempts > 1:
                print("Guess again.")
            no_of_attempts -= 1
        else:
            print("Too Low.")
            if no_of_attempts > 1:
                print("Guess again.")
            no_of_attempts -= 1
    if no_of_attempts == 0:
        print("You run out of guesses, you lose.")

elif choice == 'hard':
    no_of_attempts = 5
    while no_of_attempts > 0:
        print(f"You have {no_of_attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess == Guess:
            print(f"You got it! The answer was {Guess}.")
            no_of_attempts = -1
        elif user_guess > Guess:
            print("Too High.")
            if no_of_attempts > 1:
                print("Guess again.")
            no_of_attempts -= 1
        else:
            print("Too Low.")
            if no_of_attempts > 1:
                print("Guess again.")
            no_of_attempts -= 1
    if no_of_attempts == 0:
        print("You run out of guesses, you lose.")

else:
    print("Please type 'easy' or 'hard' only.")