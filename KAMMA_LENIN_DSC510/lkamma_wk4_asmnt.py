# File: lkamma_wk4_asmnt.py
# Course: DSC501-303 Introduction to Programming
# Assignment#: 4.1
# Author: Lenin Kamma
# Date: 04/06/2019
# Description: This program calculates the total installation cost of fiber optic cable with taxes
# discount is given if user purchases more than 100 feet of cable
# Usage: This program requires total length of the optic fiber as the input

import datetime

# Changes the color of the text to green
print("\033[1;32;48m")
print('Welcome to BellFI Optic Fiber - Best place to buy optic fiber ')
print("\033[1;30;48m")
# actual price per foot = 0.87 cents and tax= 7%
act_price = 0.87
tax = 0.07

# define function
# actual cost = original cost of the cable
# cost_after_disc = cost after deducting the discount
# cost_plus_tax   = tax added to the cost after discount

def caltotcost(ft, prc):
    act_cost = ft * act_price
    cost_after_disc = ft * prc
    cal_tax = cost_after_disc * tax
    cost_plus_tax = round(cost_after_disc + cal_tax, 2)
    print("\033[1;33;48m")
    print("Actual Cost of the Cable :  " + '%.2f' % act_cost + "$")
    if ft > 100:
        print("Total Cost of Your Purchase after discount:  " + '%.2f' % cost_after_disc + "$")
        print("Final Cost of Your Purchase(plus 7% tax): " + '%.2f' % cost_plus_tax + "$")
    inp_enter = input('Enter Y for Your Receipt : \n')

# Print receipt with company name, total cost and time
    if inp_enter in ('y', 'Y'):
        print("\033[1;32;48m")
        print("     BellFI Optic Fiber \n\t\t RECEIPT\n\t")
        print("\033[1;33;48m")
        print("\t  Buyer : " + inp_comp)
        print("Total Optic Fiber Purchased:", + no_of_feet, "ft")
        print("\t   Sub Total : " + "$" + '%.2f' % cost_after_disc)
        print("\tSales tax(7%): " + "$" + '%.2f' % cal_tax)
        print("\t  Total Cost : " + "$" + '%.2f' % cost_plus_tax)
        print("\033[1;32;48m")
        print("\nThank you for shopping BellFI!!")
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M"), "\n")
    else:
        print("Thank you. Bye")
    return cost_plus_tax

# Takes input from the user for company name and feet
inp_comp = input('Please Enter Your Company Name: \n')
while True:
    try:
        print("\033[1;30;48m")
        no_of_feet = float(input('Enter total length of optic fiber you want to purchase (In Feet) : \n'))
        break
    except ValueError:
        print("\033[1;31;48m")
        print(''"Sorry! That was not a valid number. Please try again..."'')

# calculate discount value
if no_of_feet <= 100:
    disc_val = 0                                    # No discount when total feet <= 100
else:
    if (no_of_feet > 100) and (no_of_feet <= 250):
        disc_val = 0.07                             # 7 cents discount when total feet <= 250 and > 100
    else:
        if (no_of_feet > 250) and (no_of_feet <= 500):
            disc_val = 0.17                         # 17 cents discount when total feet <= 500 and > 250
        else:
            disc_val = 0.37                         # 37 cents discount when total feet > 500

# cost per foot = actual price minus discount value
aft_dis_prc = act_price - disc_val
# call function to calculate the costs
caltotcost(no_of_feet, aft_dis_prc)
