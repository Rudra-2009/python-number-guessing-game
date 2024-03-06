#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     03/03/2024
# Copyright:   (c) HP 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random

print("Hi")
print("This is a number guessing game")

# Add a loop to play the game multiple times
while True:
    nos = random.randint(0, 1)
    y = int(input("Please enter a number: "))

    if y == nos:
        print("You are correct!")
    else:
        print("You are wrong.")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break  # Exit t if the user doesn't want to play again

print("Thanks for playing!")



