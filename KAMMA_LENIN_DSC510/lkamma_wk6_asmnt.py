# File: lkamma_wk6_asmnt.py
# Course: DSC501-303 Introduction to Programming
# Assignment#: 6.1
# Author: Lenin Kamma
# Date: 04/19/2019
# Description: This program populate the list of temperatures entered
#              Prints the highest, lowest and count of temperatures

print('Welcome!!')
temperatures = []                                       # create an empty list of temperatures

while True:                                             # run this loop and build temperature list
    in_temp = str(input('Enter Temperature: \n'))       # take input
    if in_temp.isnumeric():                             # if input is numeric build the list else exit
        temperatures.append(in_temp)
    else:
        break

if len(temperatures) == 0:                              # if the list is empty print a good bye message
    print("No temperatures entered. Good bye")
else:                                                   # if the list is not empty print max, min and count
    print("Largest Temperature entered by you: ", max(temperatures))
    print("Smallest Temperature entered by you: ", min(temperatures))
    print("Number of Temperature entered by you: ", len(temperatures))




