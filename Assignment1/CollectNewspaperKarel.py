from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    move()
    turn_karel_right()
    move()
    turn_left()
    move()
    move()
    pick_beeper()

def turn_karel_right():
    turn_left()
    turn_left()
    turn_left()
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
