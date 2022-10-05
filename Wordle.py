# File: Wordle.py

"""
WORDLE 
Abbie Luper, Spencer King, Logan Kimball, Samantha Prettyman, Zachary Barton

"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    wordleWord = random.choice(FIVE_LETTER_WORDS)

    print(wordleWord)

    def enter_action(s):

        row = 0
        col = 0
        guess = ""

        # ITERATE THROUGH EACH COLUMN OF GIVEN ROW
        for col in range(5):
            guess += gw.get_square_letter(gw.get_current_row(), col)
            col += 1

        # SEE IF THE WORD IS LEGITIMATE
        if guess.lower() in FIVE_LETTER_WORDS:
            print("Hurray! Guess " + guess + " was found in word list")

            # CHANGE COLOR OF BOXES IF WORD IS LEGITIMATE
            for col in range(5):
                if gw.get_square_letter(gw.get_current_row(), col).lower() == wordleWord[col]:
                    gw.set_square_color(gw.get_current_row(), col, '#66BB66')
                elif gw.get_square_letter(gw.get_current_row(), col).lower() in wordleWord:
                    gw.set_square_color(gw.get_current_row(), col, '#CCBB66')
                else:
                    gw.set_square_color(gw.get_current_row(), col, '#999999')  

            # MESSAGE FOR WHEN THEY GET THE CORRECT WORD
            if guess.lower() == wordleWord.lower():
                gw.show_message("Congrats! You guessed the word!")

            gw.set_current_row(gw.get_current_row()+1)

        else:
            gw.show_message("Not in word list.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()