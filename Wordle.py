# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    wordleWord = random.choice(FIVE_LETTER_WORDS)

    # MILESTONE 2
    def enter_action(s):
    
        row = 0
        guess = ""
        for col in range(5):
            guess += gw.get_square_letter(row, col)
            col += 1
            # print(guess)

        if guess.lower() in FIVE_LETTER_WORDS:
            print("Hurray! Guess " + guess + " was found in word list")
        else:
            gw.show_message("Not in word list.")
            

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()