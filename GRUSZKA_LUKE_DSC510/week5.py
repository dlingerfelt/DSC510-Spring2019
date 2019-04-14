'''
File: Week5.py
Name: Luke Gruszka
Date: 3/17/2019
Course: DSC510-T303 Introduction to Programming (2195-1)
Desc: User will be asked for two numbers and also an operation to perform.
        The performCalculation function will take in the two number and do the operation entered to give the output.
        The calculateAverage will take in the two numbers and give an average output of the two numbers.
        Error handling is in the except of the while loop to redo then entire operation.
Usage: The User will type in two numbers and the operation that they want to perform.
        Then output will show the output of the two number done by the operation.
'''
def performCalculation(firstNumber,secondNumber,selectOperation):
    ''' Loop to get the information '''
        while True:
            try:
                if selectOperation == '+':
                    outputValue = firstNumber + secondNumber
                    print(outputValue)
                elif selectOperation == '-':
                    outputValue = firstNumber - secondNumber
                    print(outputValue)
                elif selectOperation == '/':
                    outputValue = firstNumber / secondNumber
                    print(outputValue)
                elif selectOperation == '*':
                    outputValue = firstNumber * secondNumber
                    print(outputValue)
                elif selectOperation == 'AVERAGE':
                    '''Pass variables into function'''
                    calculateAverage(firstNumber,secondNumber)

            except Exception as e:
                ''' Reenter the information until correct '''
                noGood = raw_input('Renter valid numbers and operation method. Press Enter to continue.')
                firstNumber = int(raw_input('Type in the first number: '))
                secondNumber = int(raw_input('Type in the second number: '))
                selectOperation = raw_input('Enter in a following operation to do. (+, -, /, *, or AVERAGE)')
                continue

            else:
                break

def calculateAverage(firstNumber,secondNumber):
    '''Algorithm to get the average'''
    averageNumber = (firstNumber+secondNumber)/2
    print(averageNumber)

'''User inputs below'''
firstNumber = int(raw_input('Type in the first number: '))
secondNumber = int(raw_input('Type in the second number: '))
selectOperation = raw_input('Type in the symbol for the operation (+, -, /, *, or AVERAGE): ')

'''Pass variables into function'''
performCalculation(firstNumber,secondNumber,selectOperation)
