'''
File: Week2.py
Name: Luke Gruszka
Date: 3/17/2019
Course: DSC510-T303 Introduction to Programming (2195-1)
Desc: Using comments, create a header at the top of the program indicating the purpose of the program, assignment number, and your name. Use the SIUE Style Guide as a reference.
      Display a welcome message for your user.
      Retrieve the company name from the user.
      Retrieve the number of feet of fiber optic cable to be installed from the user.
      Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
      Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.
      Include appropriate comments throughout the program.
Usage: The User will type in the Company Name and a valid number. Then output will show a summary of the description.
'''

comName = raw_input("Welcome to the program, please enter your Company Name: ") or 'N/A'
numFiber = raw_input("Enter the number of feet of fiber optic cable to be installed from the user: ")
while True:
    try:

        fiberFeet = int(numFiber)
        if fiberFeet < 100:
            installCost = fiberFeet * .87

        totalCost = fiberFeet + installCost
        print('Company Name: ' + str(comName) + '\n' + 'Feet of Fiber Optic Cable: ' + str(
            fiberFeet) + 'ft'+'\n' + 'Installation Cost ' + '${:,.2f}'.format(
            installCost) + '\n' + 'Total Cost: ' + '${:,.2f}'.format(totalCost))

    except ValueError:
        numFiber = raw_input("ERROR: Enter the number of feet of fiber optic cable to be installed from the user: ")
        continue

    else:
        break

'''
Below is the explanation of '${:,.2f}' : 
The :, adds a comma as a thousands separator so it will keep format in the thousands and above with commas 
The .2f limits the string to two decimal places to match the currency format 

The while loop is used to cycle through the try statement until the correct format for feet is used. Has to be numeric.
Standard output is Company name, Feet of Fiber optic, Installation cost, and total cost.
'''