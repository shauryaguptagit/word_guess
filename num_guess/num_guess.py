"""
Build a Number guessing game, in which the user selects a range.
Lets say User selected a range, i.e., from A to B, where A and B belong to Integer.
Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses
"""
import random

print("WELCOME TO THE NUMBER GUESSR!")
print("You have to select a range from which a random number will be selected,\nthen you have to guess that number.")
print("The range should contain more than or equal to 5 numbers")
start = input("Start the game? (Y/N)").capitalize
if start != 'Y':
    print("We will hope to see you again!")
else:
        a = int(input("Enter the Lower Bound of the Range: "))
        b = int(input("Enter the Upper Bound of the Range: "))