# File: lkamma_wk3_asmnt.py
# Course: DSC501-303 Introduction to Programming
# Assignment#: 3.1
# Author: Lenin Kamma
# Date: 03/29/2019
# Description: This program calculates the total installation cost of fiber optic cable with taxes
# discount is given if user purchases more than 100 feet of cable
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
        no_of_feet = float(input('Enter total length of optic fiber you want to purchase (In Feet) : \n'))
        break
    except ValueError:
        print("\033[1;31;48m")
        print(''"Sorry! That was not a valid number. Please try again..."'')

# Calculates the discount value per foot that needs to be applied
if no_of_feet <= 100:
    disc_val = 0
else:
    if (no_of_feet > 100) and (no_of_feet <= 250):
        disc_val = 0.07
    else:
        if (no_of_feet > 250) and (no_of_feet <= 500):
            disc_val = 0.17
        else:
            disc_val = 0.37

# Calculates the cost, sales tax and total cost rounded to nearest dollar
cal_cost = round(no_of_feet * 0.87, 2)                              # Actual cost of the cable
total_disc = round(no_of_feet * disc_val, 2)                        # Total Discount
cost_after_disc = round(cal_cost - total_disc, 2)                   # Cost after discount
cal_tax = round(cost_after_disc * 0.07, 2)                          # Tax calculated
final_cost = round(cost_after_disc + cal_tax, 2)                    # Final cost (includes tax)
print("\033[1;33;48m")
print("Actual Cost of the Cable :  " + '%.2f' % cal_cost + "$")
if no_of_feet > 100:
    print("Total Discount applied   : " + "-"+'%.2f' % total_disc + "$")
    print("Sub Total                :  " + '%.2f' % cost_after_disc + "$")
print("Total Cost of Your Purchase(plus 7% tax): " + '%.2f' % final_cost+"$")
inp_enter = input('Enter Y for Your Receipt : \n')

# Print receipt with company name, total cost and time
if inp_enter in ('y', 'Y'):
    print("\033[1;32;48m")
    print("     BellFI Optic Fiber \n\t\t RECEIPT\n\t")
    print("\033[1;33;48m")
    print("\t  Buyer : " + input_company)
    print("Total Optic Fiber Purchased:", + no_of_feet, "ft")
    print("\t   Sub Total : " + "$" + '%.2f' % cost_after_disc)
    print("\tSales tax(7%):  " + "$" + '%.2f' % cal_tax)
    print("\t  Total Cost : " + "$" + '%.2f' % final_cost)
    print("\033[1;32;48m")
    print("\nThank you for shopping BellFI!!")
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M"), "\n")
else:
    print("Thank you. Bye")


