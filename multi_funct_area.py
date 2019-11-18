#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: November 2019
# This program calculates area of a triangle


def area(height, base):
    # calculates area of a triangle

    # process
    triangle_area = (height * base)/2

    # output
    print("")
    print("The area of the triangle is {0} cm^2".format(triangle_area))


def main():
    # this function just calls other functions

    # input
    try:
        print("Let's find the area of a triangle!")
        height_from_user = int(input("Enter the height of a triangle: "))
        base_from_user = int(input("Enter the base of a triangle: "))

        # call functions
        area(height_from_user, base_from_user)

    except Exception:
        print("")
        print("Wrong input. Try again with an integer!")


if __name__ == "__main__":
    main()
