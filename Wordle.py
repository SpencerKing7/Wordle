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
    guessNum = 0

    # MILESTONE 2
    def enter_action(guessNum):
    
        guess = ""
        for col in range(5):
            guess += gw.get_square_letter(guessNum, col)
            col += 1
            # print(guess)

        if guess.lower() in FIVE_LETTER_WORDS:
            print("Hurray! Guess " + guess + " was found in word list")
            for col in range(5):
                if gw.get_square_letter(guessNum, col).lower() == wordleWord[col]:
                    gw.set_square_color(guessNum, col, '#66BB66')
                elif gw.get_square_letter(guessNum, col).lower() in wordleWord:
                    gw.set_square_color(guessNum, col, '#CCBB66')
                else:
                    gw.set_square_color(guessNum, col, '#999999')                

        else:
            gw.show_message("Not in word list.")
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action(guessNum))

# Startup code

if __name__ == "__main__":
    wordle()