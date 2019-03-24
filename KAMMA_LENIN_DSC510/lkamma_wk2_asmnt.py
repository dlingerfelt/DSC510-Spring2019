# File: lkamma_wk2_asmnt.py
# Course: DSC501-303 Introduction to Programming
# Assignment#: 2.1
# Author: Lenin Kamma
# Date: 03/24/2019
# Description: This program calculates the total installation cost of fiber optic cable with taxes
# Usage: This program requires total length of the optic fiber as the input

import datetime

# Changes the color of the text to green
print("\033[1;32;48m")
print('Welcome to BellFI Optic Fiber - Best place to buy optic fiber ')
print("\033[1;30;48m")

# Takes Input from the user for company name and feet
input_company = input('Please Enter Your Company Name: \n')
while True:
    try:
        print("\033[1;30;48m")
        input_no_of_feet = float(input('Enter total length of optic fiber you want to purchase (In Feet) : \n'))
        break
    except ValueError:
        print("\033[1;31;48m")
        print(''"Sorry! That was not a valid number. Please try again..."'')

# Calculates the cost, sales tax and total cost rounded to nearest dollar
cal_cost = round(input_no_of_feet * 0.87, 2)
cal_tax = round(cal_cost * 0.07, 2)
tot_cost = round(cal_cost + cal_tax, 2)
print("\033[1;33;48m")
print("Total Cost of your Purchase (plus 7% tax): " + str(tot_cost)+"$")
inp_enter = input('Enter Y for Your Receipt : \n')

# Print receipt with company name, total cost and time
if inp_enter in ('y', 'Y'):
    print("\033[1;32;48m")
    print("     BellFI Optic Fiber \n\t\t RECEIPT\n\t")
    print("\033[1;33;48m")
    print("\t  Buyer : " + input_company)
    print("Total Optic Fiber Purchased:", input_no_of_feet, "ft")
    print("\t   Sub Total : " + "$" + str(cal_cost))
    print("\tSales tax(7%): " + "$ " + str(cal_tax))
    print("\t  Total Cost : " + "$" + str(tot_cost))
    print("\033[1;32;48m")
    print("\nThank you for shopping BellFI!!")
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M"), "\n")
else:
    print("Thank you. Bye")


