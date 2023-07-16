#!/usr/bin/python3
"""Importing modules """
import math
import sys


def calculate_hypotenuse(a, b):
    """Calculate the hypotenuse of a right triangle."""
    return math.sqrt(a ** 2 + b ** 2)


def main():
    """Entry point of the program."""
    try:
        side_a = float(input("Enter the length of side A: "))
        side_b = float(input("Enter the length of side B: "))
        hypotenuse = calculate_hypotenuse(side_a, side_b)
        print("The length of the hypotenuse is:", hypotenuse)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        sys.exit(1)


if __name__ == "__main__":
    main()

