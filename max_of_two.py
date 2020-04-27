################################################################################
# Author: Addison Lawrence
# Date: 2/17/2020
# Chooses the largest number when given two
################################################################################

def max_of_two(number1,number2):#function to find which number is larger
    if number1>number2:
        print(number1,'is greater.')
    elif number2>number1:
        print(number2,'is greater.')
    elif number1==number2:
        print('The numbers are equal.')


number1=int(input('Enter the first integer: '))#number 1 input
number2=int(input('Enter the second integer: '))#number 2 input
max_of_two(number1,number2)#function call
