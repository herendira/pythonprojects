"""
# File: fuel_usage.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose: Functions

"""

def main():
    # Get an odometer value in U.S. miles from the user.
    start_miles=float(input("Enter the first odometer reading (miles): "))
    # Get another odometer value in U.S. miles from the user.
    end_miles=float(input("Enter the second odometer reading (miles): "))
    # Get a fuel amount in U.S. gallons from the user.
    amount_gallons=float(input("Enter the amount of fuel used (gallons): "))
    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    named_mpg=miles_per_gallon(start_miles, end_miles, amount_gallons)
    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k=lp100k_from_mpg(named_mpg)
    # Display the results for the user to see.
    print(f"{named_mpg:.2f} miles per gallon")
    print(f"{lp100k:.2f} liters per 100 kilometers")
    #pass


def miles_per_gallon(start_miles, end_miles, amount_gallons):
     named_mpg=(end_miles-start_miles)/amount_gallons
     return named_mpg


def lp100k_from_mpg(named_mpg):
    lp100k=235.215/named_mpg
    return lp100k


# Call the main function so that
# this program will start executing.
main()