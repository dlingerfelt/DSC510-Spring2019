

"""
 Purpose of the program: calculating the total installation cost of fiber optic cable
 Assignment number: 2.1
 Name: Srilakshmi Bodduluru
"""

#welcome message for user
print("Welcome User")

#Retrieve the company name from the user
company_name=input('what is your company name?')

#Retrieve the number of feet of fiber optic cable to be installed from the user
cable_length=input('what is the length of fiber optic cable needed in feet?')

#Calculate the installation cost of fiber optic cable
total_installation_cost=float(cable_length)*0.87

#get date& time
import datetime
now = datetime.datetime.now()

#print receipt
print('\t ------------------------')
print('\t !!!!!Receipt!!!!!')
print('\t ------------------------')
print('\t Date&Time:\t',str(now))
print('\t company name :',company_name)
print('\t length of the cable in feet:',cable_length)
print('\t total cost:$',total_installation_cost)