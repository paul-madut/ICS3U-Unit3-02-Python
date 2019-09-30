#!/usr/bin//env python3

# Created on: September 2019
# Created by: Paul Madut
# This is the a program used as a random number generator


def main():
    # This function does plays a game
    # Input
    number_guessed = int(input("Enter a number to play: "))
    print(" ")
    # Process
    if number_guessed == 5:
        print("Congrats you right dawg.")
    else:
        print("You are a failure.")


if __name__ == "__main__":
    main()
