#Build a Word Guessing Game with Python

import random

#Word Bank
word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']

#Word To Guess
word = random.choice(word_bank)

#To make spaces for the chosen word
guessedWord = ['_'] * len(word)

#how many attempts to solve the puzzle
attempts = 10

#Inner Working of Game

while (attempts > 0):
    print("\nCurrent Word: " + ''.join(guessedWord))
    guess = input("Enter a Letter: ")

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print("Great Guess!")
    
    else:
        attempts -= 1
        print("Wrong Guess! Attempts Left: " + str(attempts))

    if '_' not in guessedWord:
        print("\nCongratulations!! You guessed the word: " + word)
        break

    else:
        print("\nYou\'ve run out of attempts! The word was: " + word)