from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    """
    Karel paint the exterior of some oddly-shaped buildings using beepers!
    Karel should paint one side of the rectangle,
    placing beepers on all corners that are adjacent  to  the  wall  of  the  building.
    Karel will move as long there is unpainted wall.
    """
    while no_beepers_present():
        move_check()


def move_check():
    """
    Karel will move based on theese condition
    :return:
    """
    if left_is_clear():
        left_drift()
        paint_wall()
    if front_is_blocked():
        turn_right()
        paint_wall()
    if facing_west and front_is_blocked():
        left_drift()
        if beepers_present():
            turn_around()
            move()
        else:
            paint_wall()
    if facing_east and front_is_blocked():
        left_drift()
        paint_wall()
    else:
        paint_wall()


def turn_right():
    """
    Karel  will turn right
    :return:
    """
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    """
    Karel will turn around
    :return:
    """
    turn_left()
    turn_left()


def left_drift():
    """
    In the corner Karel will turn left and move
    :return:
    """
    turn_left()
    move()


def paint_wall():
    """
    If there is no beeper, Karel will paint the wall
    :return:
    """
    if no_beepers_present():
        while left_is_blocked():
            put_beeper()
            move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
