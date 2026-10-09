#!/usr/bin/env python3
# Created By: Emmanuella Taiwo
# created on 9th Oct, 2026
# This program asks the for a number between 0 and 9 and
#  checks if the input is valid or not. If the input is valid,
#  it will display the number back to the user.
import constants


def main():
    # get the number from the user and convert to an integer
    number = int(input("Enter a number between 0 and 9: "))

    # check if the number is between 0 and 9
    if number < 0 or number > 9:
        print("you are wrong. try again.")
    else:
        if number == constants.CORRECT_ANSWER:
            print("You are correct: {0}".format(number))
        else:
            print("You are wrong. try again.")


if __name__ == "__main__":
    main()
