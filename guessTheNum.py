#!/usr/bin/env python3

# Programmer: Laith Abou Saleh
# this is a guessing game that gives the user
# 10 guesses to guess a 3 digit random number 

import random

NUM_DIGITS = 3  
MAX_GUESSES = 10


def main():
    print(""" I have a secret number and you need
    to guess it to win the game!
    These are the given hints that you can see:
        1. RIGHT: there is a correct number in the correct position
        2. MAYBE: there is a correct number in the wrong position
        3. WRONG: incorrect number
    """)

    # game loop that loops until user decides to stop plaing
    while True:
        
        # generating a random number
        secret_number = get_secret()
        print(f"I am thinking of a number of {NUM_DIGITS} digits right now!")
        print("try to guess it.")

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            
            guess = ''

            # this loop checks if input is valid 
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess # {numGuesses}")
                guess = input("> ")

            # getting the hints for the user
            hints = get_hints(guess, secret_number)
            numGuesses += 1
            print(hints)

            if guess == secret_number:
                break
            if numGuesses > MAX_GUESSES:
                print("You have used all your guesses!")
                print("YOU LOST")
        
        print("Do you want to play again? (yes or no)")
        ans = input('> ').lower
        if ans[0] != 'y':
            break
    print("Thanks for plaing :)")


# this function returns a 3 digit string as 
# the number to be guessed
def get_secret():

    numbers = list('0123456789')
    random.shuffle(numbers)
    
    secret = ''
    for i in range(NUM_DIGITS):
        secret += str(numbers[i])

    return secret

# this function gives hints to the user on how 
# close they are from getting the right answer 
def get_hints(guess, secrect):
    
    if guess == secrect:
        return "You got the Number!"
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secrect[i]:
            clues.append('RIGHT')
        elif guess[i] in secrect:
            clues.append("MAYBE")
    
    if len(clues) == 0:
        return "WRONG"
    else:
        clues.sort()
        return ' '.join(clues)

if __name__== '__main__':
    main()