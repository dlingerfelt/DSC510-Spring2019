# File: lkamma_wk5_asmnt.py
# Course: DSC501-303 Introduction to Programming
# Assignment#: 5.1
# Author: Lenin Kamma
# Date: 04/12/2019
# Description: This program calculates the addition, subtraction, multiplication, division, and average

print('Welcome!! Here You Can Perform Arithmetic Operations')
num_list = ['+', '-', '*', '/']
while True:                                                 # Run this loop until user enters a valid operator
    try:
        in_opr = str(input('Enter one of the operators(+ for add, - for Subtract, * for Multiply, / for Divide): \n'))
        if in_opr in num_list:
            break
        else:
            continue
    except:
            continue


def performCalculation(oprn):                               # This function calculates different Arithmetic operations
    while True:
        try:
            in_num1 = int(input('Enter First Number: \n'))      # Input first number
            break
        except ValueError:
            print('Not an Integer. Please Enter Again!! \n')
    while True:
        try:
            in_num2 = int(input('Enter Second Number: \n'))     # Input second number
            break
        except ValueError:
            print('Not an Integer. Please Enter Again!! \n')

    if oprn == '+':                                             # Performs addition
        result = in_num1 + in_num2
    else:
        if oprn == '-':                                         # Performs subtraction
            result = in_num1 - in_num2
        else:
            if oprn == '*':
                result = in_num1 * in_num2                      # Performs multiplication
            else:
                if oprn == '/':
                    result = round(in_num1 / in_num2, 2)        # Performs division
    print('Result = ', result)
    return result


performCalculation(in_opr)                                      # Invokes arithmetic function


def calculateAverage():                                          # Calculates the Average and sum
    print('Now You Can Calculate the Sum and Average of Numbers')
    while True:
        try:
            inp = int(input('Enter total numbers you want to enter: \n'))    # Input total numbers
            if inp == 0:
                print('Enter Number Greater Than Zero \n')
                continue
            break
        except ValueError:
            print('Not an Integer. Please Enter Again!! \n')
    num_sum = 0
    for i in range(0, inp):                                     # for loop where inp = total numbers entered
        num_inp = int(input('Enter Number: \n'))                # Enter numbers one by one
        num_sum = num_sum + num_inp                             # Calculates sum here
    average = num_sum / inp                                     # Calculates average
    print("Sum of the numbers =", num_sum)
    print("Average of the numbers =", round(average, 2))


calculateAverage()                                              # Invokes average



