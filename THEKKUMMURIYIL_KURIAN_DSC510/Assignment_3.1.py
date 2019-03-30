# Purpose           : This program calculates the cost of fiber optic cable installation
#                     based on user inputted the number of feet of cable to be installed,
#                     applies discount based on the user inputted number of feet of installation needed
#                     and prints the receipt.
# Assignment Number : 3.1
# Author            : Tinto T. Kurian


# gets the current date and time.
import datetime
current_date = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")

# Generates a random number in the given range to be used as receipt number
import random
receipt_number = random.randint(1001,999999)

cost_per_feet = 0.87  # Cost of per feet of installation.
tax = 7               # % of tax.
name_of_our_company = 'Fiber Connections'
our_company_address = 'xyz Street, Phoenix, AZ 85555'
our_company_phone = '(440) 555 123'

# Defining characters into variable to later do arithmetic operation for print formatting.
star = '*'
tab = '\t'
line = '-'

# Prints a welcome message to the user
print(star*100)
print('{0}WELCOME TO {1}'.format(tab*6, name_of_our_company.upper()))
print(star*100)

# Gets the Company name of the user.
user_company_name = input('Please enter the name of your company:\n')

# Gets the length of fiber optic to be installed and ensures it is a numeric value,
# prompts to enter again if the input in invalid
while True:
    try:
        num_of_feet = float(input('Please enter, the length of fiber optic you want installed, in feet :\n'))
        break
    except ValueError:
        print('Not a valid input, Please enter a number')

# Calculates the discount based on the number of feet of installation the user needs installed.
if num_of_feet > 500:
    cost_per_feet = 0.50
elif num_of_feet > 250:
    cost_per_feet = 0.70
elif num_of_feet > 100:
    cost_per_feet = 0.80
else:
    cost_per_feet = 0.87

# calculates the cost of installation ( No: of feet * cost_per_feet) and rounds it to two decimal values
cost_of_installation = round(num_of_feet * cost_per_feet, 2)

# calculates the tax by applying the tax % on calculated cost of installation.
calculated_tax = round(cost_of_installation*(tax/100), 2)

# Prints the receipt, with
# 1. Name of our company, Address and phone# as header.
# 2. Date
# 3. Receipt issued for , with user's company name
# 4. Prints a Receipt #, which is a random generated number.
# 5. Length of the fiber optic installed
# 6. Calculated cost of installation with details of per foot charge.
# 7. Tax for the calculated cost of Installation, based on the Tax %
# 8. Total cost ( Tax + Cost of Installation)

print(star*100)
print('{0}{1}'.format(tab*8, name_of_our_company.upper()))
print('{0}{1}'.format(tab*6, our_company_address))
print('{0}{1}'.format(tab*8, our_company_phone))
print(star*100)
print('Date: {}'.format(current_date))
print('Receipt for: {}'.format(user_company_name.upper()))
print('Receipt #: {}'.format(receipt_number))
print(line*100)
print('Length of fiber optic installed:  {} Feet'.format(num_of_feet))
print('Cost of installation:{0} ${1}'.format(tab*3, cost_of_installation))
print('{0}@ ${1} per foot'.format(tab,cost_per_feet))
print('Tax {0}%:{2} ${1}'.format(tax, calculated_tax, tab*7))
print(line*100)
print('Total Cost:{0} ${1}'.format(tab*6, round(cost_of_installation+calculated_tax,2)))
print(line*100)
print('{0}{1}'.format(tab*6, 'THANK YOU! FOR YOUR BUSINESS'))
print(star*100)

