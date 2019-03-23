"""
File: Assignment_2.1.py
Author: Holly Erickson
Date: 2019-03-23
Course: DSC 510-T303 Intro to Programming
Assignment: 2.1
Desc: This program display a welcome message. Then retrieves a company name &
    the number of feet of fiber optic cable to be installed from the user.
    It calculate the installation cost and prints a receipt for the user.
Usage: Prompts user for input, performs calculations and outputs a receipt for fiber optic cable installed.
"""

import datetime
from decimal import localcontext, Decimal, ROUND_HALF_UP

# Global variables
install_rate = 0.87
tax_rate = 0.06


def round_half_up(number):
    """
    This takes a number and rounds it to two decimal places.
    I did it this way instead of using round() to avoid rounding down at .xx5
    """
    with localcontext() as ctx:
        ctx.rounding = ROUND_HALF_UP
        two_places = Decimal("0.01")
        return Decimal(str(number)).quantize(two_places)


print("\nWelcome to 'Always Online', the fiber optic cable store! ")
print("Our premium performance fiber optic cable costs $0.87 per foot including installation. \n")

# Retrieve the company name from the user.
company = input("Please enter your company name: \n")

# Retrieve the number of feet of fiber optic cable to be installed from the user. Ensures valid numeric input.
while True:
    try:
        feet = input("Please enter the number of feet of fiber optic cable you would like installed: \n")
        feet = float(feet)
        break
    except ValueError:
        print("Error: Not a valid number.")

# Calculate the installation cost and sales tax.
calculated_cost = (feet * install_rate)
tax = (calculated_cost * tax_rate)
calculated_cost = round_half_up(calculated_cost)
tax = round_half_up(tax)

# Print a receipt for the user including company name, number of feet to be installed, calculated cost, & total cost.
print("\nReceipt from Always Online")

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"), "\n")

print("Company name:", company)
print("Number of feet to be installed:", feet, "feet")
print("Calculated cost: $%s" % calculated_cost)
print("Sales tax:       $%s" % tax)
print("Total cost:      $%s" % round_half_up(calculated_cost+tax))

print("\nThank you for shopping!")










