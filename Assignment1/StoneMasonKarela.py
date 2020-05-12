from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    up_down()
    go_horizon()
    up_down()
    go_horizon()
    up_down()
    go_horizon()
    up_down()


def up_down():
    turn_left()
    beepers_fix()
    turn_around()
    while front_is_clear():
        move()


def beepers_fix():
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        move()
        take_beeper_again()
    put_beeper()


def take_beeper_again():
    if beepers_present():
        pick_beeper()


def go_horizon():
    turn_left()
    for i in range(4):
        move()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
