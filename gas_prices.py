################################################################################
# Author: Addison Lawrence
# Date: 4/19/2020
# Reads file of gas prices over 52 weeks and plots them 
################################################################################

import matplotlib.pyplot as plt#import matplotlib

gasprice=[]#intialize gasprice
weeks=list(range(1,53))#create list of week numbers

with open('2008_Weekly_Gas_Averages.txt') as fo:#open price file
    for line in fo:
        gasprice.append(float(line.rstrip()))#add each price to a list

fig, prices=plt.subplots()#begin plot figure
prices.plot(weeks,gasprice)#plot week and gasprice
prices.set_title('2008 Weekly Gas Prices')#plot title
prices.set_ylabel('Average Price (dollars/gallon)')#y label
prices.set_xlabel('Weeks (by number)')#x label
prices.set_xticks([10,20,30,40,50])#set x tick marks
prices.set_yticks([1.5,2.0,2.5,3.0,3.5,4.0])#set y tick marks
prices.set_xlim(1,52)#set y limit
prices.set_ylim(1.5,4.25)#set x limit
plt.grid()#turn on grid
plt.show()#show plot
