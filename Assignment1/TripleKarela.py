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

   blok_left()
   turn_left()
   move()
   blok_left()
   turn_left()
   move()
   depan_clear()
   turn_right()
   blok_left()
   turn_left()
   move()
   blok_left()
   turn_left()
   move()
   depan_clear()
   turn_right()
   blok_left()
   turn_left()
   move()
   blok_left()
   turn_left()
   move()
   blok_left()
def turn_right():
   turn_left()
   turn_left()
   turn_left()

def blok_left():
    while left_is_blocked():
        put_beeper()
        move()
def depan_clear():
    while front_is_clear():
        put_beeper()
        move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
