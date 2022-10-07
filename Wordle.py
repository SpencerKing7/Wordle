# File: Wordle.py

"""
WORDLE 
Abbie Luper, Spencer King, Logan Kimball, Samantha Prettyman, Zachary Barton
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR

def wordle():
    wordleWord = random.choice(FIVE_LETTER_WORDS)
    gw = WordleGWindow()

    print(wordleWord)

    def is_unknown(x):
        return True if gw.get_key_color(x) == UNKNOWN_COLOR else False

    def enter_action(guess):
        hasWon = False
        i = 0

        # SEE IF THE WORD IS LEGITIMATE
        if guess.lower() in FIVE_LETTER_WORDS:
            print("Hurray! Guess " + guess + " was found in word list")

            # MESSAGE FOR WHEN THEY GET THE CORRECT WORD
            if (guess.lower() == wordleWord):
                hasWon = True
                gw.show_message("Congrats! You guessed the word!")
            
            # CHANGE COLOR OF BOXES IF WORD IS LEGITIMATE
            for letter in wordleWord:
                if letter == guess[i].lower():
                    gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
                    
                    if is_unknown(guess[i]):
                        gw.set_key_color(guess[i], CORRECT_COLOR)
                elif guess[i].lower() in wordleWord:
                    gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
                    
                    if is_unknown(guess[i]):
                        gw.set_key_color(guess[i], PRESENT_COLOR)
                else:
                    gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)
                    
                    if is_unknown(guess[i]):
                        gw.set_key_color(guess[i], MISSING_COLOR)
                
                i += 1
            
            # INCREMENT ROW
            if not hasWon:
                gw.set_current_row(gw.get_current_row() + 1)
        else:
            gw.show_message("Not in word list.")
    
    gw.set_current_row(0)
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()