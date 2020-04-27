################################################################################
# Author: Addison Lawrence
# Date: 2/29/2020
# Gives a math quiz with two randomly generated numbers
################################################################################



from random import *#inport the random module

number1=randint(10,99)#chooses a random 2 digit number
number2=randint(100,999)#chooses a random 3 digit number
print(' ',format(number1,'>3'),'\n+',format(number2,'>3'))#prints the numbers
guess=int(input('= '))#user input guess
answer=number1+number2#calculate the answer

#if correct print correct and if not then give the answer
if guess==answer:
    print('Correct answer -- Good Work!')
else:
    print('Incorrect... The correct answer is:',answer)
