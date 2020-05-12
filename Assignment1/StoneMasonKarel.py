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
    """
    Karel will  repair the damage done to the Main Quad in the 1989 Loma Prieta earthquake.
    This function will do repair four times.
    """
    for i in range(3):
        repair_arc()
        next_arc()
    repair_arc()


def repair_arc():
    """
    Karel will repair arc and return to ground state
    Precondition & Post-condition : Karel facing east
    :return:
    """
    turn_left()
    climb_up()
    turn_around()
    climb_down()
    turn_left()


def climb_up():
    """
    Karel will climb up and patch the arc
    :return:
    """
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
            move()
        else:
            move()
    if front_is_blocked and no_beepers_present():
        put_beeper()


def climb_down():
    """
    Karel will climb down after repair the arc,
    and will stop if blocked by wall
    :return:
    """
    while front_is_clear():
        move()


def turn_around():
    """
    Karel will turn around
    :return:
    """
    turn_left()
    turn_left()


def next_arc():
    """
    Karel will move into next arc
    :return:
    """
    move()
    move()
    move()
    move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
