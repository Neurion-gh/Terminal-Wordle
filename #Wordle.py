#Wordle

import random
from termcolor import colored
import string

wordle_words = [

    "apple", "baker", "candy", "delta", "earth", "flame", "grape", "haste", "input", "jolly",
    "knack", "liver", "moist", "nears", "plumb", "quilt", "rusty", "stone", "trial", "unite",
    "vexed", "waste", "youth", "zesty", "chore", "dried", "equal", "firer", "goose", "hasps",
    "inked", "jumpy", "laced", "mirth", "plaza", "rival", "shiny", "toxic", "vivid", "whale"

]

word = random.choice(wordle_words)
user_input = ""
guessed_words = set()
print("Please type exit if you would like to end the game.")
attempts = 6

while user_input != "exit":
    user_input = input("\nWhat word would you like to guess?").lower()
    print(f"Attempts left: {attempts}")

    if user_input == "exit":
        print("\nYou chose to end the game")
        break
        
    if len(user_input) != 5:
        print("\nYou need to guess a word that is 5 letters long.")
        continue #continue restarts the loop, so it can be used in these kind of validation checks
        
    if user_input in guessed_words:
        print("\nYou already guessed that word.")
        continue
        
    if any(letter not in string.ascii_lowercase for letter in user_input):
            print("\nPlease chose a valid word.")
            continue

    attempts = attempts-1

    for (i, letter) in enumerate(user_input):
        if letter == word[i]: #this checks if each guessed letter is the same as the letter in the same position in the actual word
            print(colored(letter, "green"), end="") #this prints the each letter coloured correctly and ends each printout without a /n (new line)
        elif letter in word:
            print(colored(letter, "yellow"), end="") #the colored function does not assign a colour to the object forever but for a single print, hence why it has to be handled like this
            #I want to handle duplicates better, ie. only the correct number of letters present in the word will be coloured
        else: 
            print(colored(letter, "grey"), end="")
    print()
    guessed_words.add(user_input)
    
    if user_input == word:
        print(f"\n You win!")
        break
    if attempts == 0:
        print(f"\nYou ran out of attempts. \n The word was {word}")
        break

