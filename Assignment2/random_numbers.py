"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random


def main():
    """
    This program will prints 10random integers (each random integershould have a valuebetween 0 and 100, inclusive).
    """
    for i in range(10):
        print(random.randint(0, 100))




# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
