"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    subtract(5.5, 2.1)


def subtract(a, b):
    """
    This function will reads two real numbers from the user and prints the first number minus the second number
    """
    a -= b
    print (a)
    return a


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
