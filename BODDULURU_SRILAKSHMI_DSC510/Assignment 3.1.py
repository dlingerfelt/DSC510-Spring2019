
"""

 Purpose of the program: calculating the total installation cost of fiber optic cable using "if statements"
 Assignment number: 3.1
 Name: Srilakshmi Bodduluru

 """

#welcome message for user
print("Hello User")

#Retrieve the company name from the user
company_name=input('what is your company name?')

#Retrieve the number of feet of fiber optic cable to be installed from the user
cab_len = input('what is the length of fiber optic cable needed in feet?')

# using try-exception block:
try:
    cable_length = float(cab_len)
    #Calculate the installation cost of fiber optic cable
    if(cable_length > 500):
        total_installation_cost = (cable_length) * 0.5
    elif(cable_length > 250):
        total_installation_cost = (cable_length) * 0.7
    elif(cable_length > 100):
        total_installation_cost = (cable_length) * 0.8
    else:
        total_installation_cost = (cable_length) * 0.87

    # get date& time
    import datetime

    now = datetime.datetime.now()

    # print receipt
    print('\t ------------------------')
    print('\t !!!!!Receipt!!!!!')
    print('\t ------------------------')
    print('\t Date&Time:\t', str(now))
    print('\t company name :', company_name)
    print('\t length of the cable in feet:', cable_length)
    print('\t total cost:$', total_installation_cost)

except:
    print("Please enter a number for cable length")