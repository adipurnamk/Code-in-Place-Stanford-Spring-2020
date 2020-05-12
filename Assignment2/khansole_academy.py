"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random


def main():
    """
    This program will  randomly
    generates simple addition problems for the user, reads in the answer from the user, and then
    checks to see if they got it right or wrong, until the user appears to have mastered the
    material. Note that “console” is another name for “terminal” :-)
    """

    hit = 0
    while hit < 3:
        question()
        input_answer()

        if user_answer == real_answer:
            hit += 1
            print(f'Correct!  You\'ve gotten {hit} correct in a row.')
        else:
            hit = 0
            print(f'Incorrect.  The expected answer is {real_answer}')

    else:
        print('Congratulations! You mastered addition.')


def question():
    r1 = random.randint(0, 100)
    r2 = random.randint(0, 100)

    global real_answer
    real_answer = r1 + r2
    print(f'What is {r1} + {r2}?')
    return real_answer


def input_answer():
    global user_answer
    user_answer = int(input())
    return user_answer



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
