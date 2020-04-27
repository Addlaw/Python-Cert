################################################################################
# Author: Addison Lawrence
# Date: 3/22/2020
# Simulates a two dice rolls a million times and returns the frequency of each total
################################################################################


def roll_d6():
    roll=randint(1,6)#chooses a random integer between 1 and 6
    return roll#resurns the number

def main():

    totals=[]#intialize the list

    for x in range(1000000):#for loop for dice rolls
        dice1=roll_d6()#dice roll one
        dice2=roll_d6()#dice roll two
        dicetotal=dice1+dice2#add the rolls together
        totals.append(dicetotal)#add the total to the end of the list

    print('Roll: Frequency')#print the header

    for x in range(2,13):#for loop to print the frequency of each roll
        numberoftotal=totals.count(x)#counts the number of totals of a certain amount
        frequency=numberoftotal/1000000#calculates the fraction frequency
        frequencyper=frequency*100#finds the percent frequency
        print(f'{x:4}:{frequencyper:6.2f}%',sep='')#prints the frequencies

from random import*#imports the random module

main()#run main function

