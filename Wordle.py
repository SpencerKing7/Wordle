# File: Wordle.py

"""
WORDLE 
Abbie Luper, Spencer King, Logan Kimball, Samantha Prettyman, Zachary Barton
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    wordleWord = random.choice(FIVE_LETTER_WORDS)
    gw = WordleGWindow()

    print(wordleWord)

    def enter_action(guess):

        # CHANGE COLOR OF BOXES
        def update_squares():
            i = 0

            for letter in wordleWord:
                if letter == guess[i].lower():
                    gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)

                    if gw.get_key_color(guess[i]) != CORRECT_COLOR:
                        gw.set_key_color(guess[i], CORRECT_COLOR)
                elif guess[i].lower() in wordleWord:
                    gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
                    gw.set_key_color(guess[i], PRESENT_COLOR)
                else:
                    gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)
                    gw.set_key_color(guess[i], MISSING_COLOR)
                
                i += 1
        
        # SEE IF THE WORD IS LEGITIMATE
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list", "red")
            return

        # MESSAGE FOR WHEN THEY GET THE CORRECT WORD
        if guess.lower() == wordleWord:
            gw.show_message("Congrats! You guessed the word!", "green")
            update_squares()
            return

        update_squares()
        gw.set_current_row(gw.get_current_row() + 1)
    
    gw.set_current_row(0)
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()