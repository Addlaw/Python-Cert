################################################################################
# Author: Addison Lawrence
# Date: 4/3/2020
# Creates a file with a specified amount of random numbers between 1 and 500
################################################################################

from random import *#import the random module

#ask for user input
numofnums=int(input('Enter the number of random numbers to be written to the file: '))
with open('random_numbers.txt', 'a') as fo:#open file to append too/create file
    for number in range(numofnums):#for loop for number of numbers
        randnum=randint(1,500)#get random nmber from 1 to 500
        fo.write(str(randnum)+'\n')#put number into file
