# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script

# Print an explanation to the user

# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"

# Ask for user input

# Allow only single-character alphabetic input

# Create a counter for how many tries a user has

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it

import random

def hangman():
    word_to_guess = "hangman"  # Hard-coded word to guess
    guessed_letters = set()
    attempts = 3  # Number of attempts allowed

    print("Welcome to Hangman!")
    print("Try to guess the word. You have 3 attempts.")

    # Display the word as a sequence of blanks
    display_word = ['_'] * len(word_to_guess)
    print(' '.join(display_word))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        # Check if the input is a single alphabetic character
        if not re.match("^[a-zA-Z]$", guess):
            print("Please enter a single alphabetic character.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue
        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in word_to_guess:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    display_word[i] = guess
            print(' '.join(display_word))
        else:
            attempts -= 1
            print(f"The letter '{guess}' is not in the word. You have {attempts} attempts left.")
            print(' '.join(display_word))

        # Check if the word has been completely guessed
        if ''.join(display_word) == word_to_guess:
            print("Congratulations! You guessed the word.")
            returns

    print(f"Sorry, you're out of attempts. The word was '{word_to_guess}'.")

hangman()