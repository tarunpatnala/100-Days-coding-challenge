import random
from replit import clear

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def select_level():
    level = input("Choose a difficulty. Type'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def guess_number(number, attempts):
    guessed = False
    while attempts > 0 and guessed != True:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if(guess == number):
            guessed = True
            print(f"You got it! The answer was {number}.")
        else:
            if(guess < number):
                print("Too low.")
            elif(guess > number):
                print("Too high.")
            attempts-=1
            if attempts >=1:
                print("Guess again.")
            else:
                print("You Lost!")

while input("Do you want to play NUMBER GUESSING game? Type 'y' to play, 'n' to pass: ") == 'y':
    clear()
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    expected_number = random.randint(1,100)
    guess_number(expected_number, select_level())


