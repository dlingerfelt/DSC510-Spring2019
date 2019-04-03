

"""

 Purpose of the program: calculating the total installation cost of fiber optic cable using functions and if statements.
 Assignment number: 4.1
 Name: Srilakshmi Bodduluru
 Date: 4/3/2019
 """

# Defining total cost calculation function with feet and price as parameters
def calculate_total_cost(cable_length, installation_cost):
    #calculating total cost
    total_cost = (cable_length) * (installation_cost)
    #prints total installation cost in $
    print("Total installation cost is :$", total_cost)
    # this function returns total installation cost
    return total_cost


#welcome message for user
print("Hello User")

#Retrieve the company name from the user
company_name=input('what is your company name?')

#Retrieve the number of feet of fiber optic cable to be installed from the user
cable_length = input('what is the length of fiber optic cable needed in feet?')

# using try-exception block to inform user if he gives wrong input:
try:
    # converting cable length to float
    cable_length = float(cable_length)
    # if cable length is greater than 500, installation cost per feet is 0.5
    if (cable_length > 500):
        installation_cost = 0.5
    # if cable length is greater than 250, installation cost per feet is 0.7
    elif (cable_length > 250):
        installation_cost = 0.7
    # if cable length is greater than 100, installation cost per feet is 0.8
    elif (cable_length > 100):
        installation_cost = 0.8
    # if cable length is less than or equal to 100, installation cost per feet is 0.87
    else:
        installation_cost = 0.87
    # using predefined function to calculate total cost
    total_installation_cost =calculate_total_cost(cable_length, installation_cost)

    # import date& time
    import datetime
    # get present date & time
    now = datetime.datetime.now()

    # print receipt with date&time,company name, cable length and total installation cost
    print('\033[1m')#prints receipt in bold
    print('\t ************************')
    print('\t !!!!!!!!Receipt!!!!!!!!!')
    print('\t ************************')
    print('\t Date&Time:\t', str(now))
    print('\t Company name :', company_name)
    print('\t Length of the cable in feet:', cable_length)
    print('\t Total cost:$', total_installation_cost)

#informs user to give number for cable length istead of showing error if he fails to give number as input
except:
    print("Please enter a number for cable length")

