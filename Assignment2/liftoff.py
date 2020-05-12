"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""


def main():
    """
    This program will prints out the calls for a spaceship that is about to launch.
    Countdown the numbers from 10 to 1 and then write “Liftoff!”
    """
    x = 10
    for i in range(11):
        a = x - i

        if a != 0:
            print(a)
        else:
            print('Liftoff!')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
