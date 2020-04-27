################################################################################
# Author: Addison Lawrence
# Date: 4/3/2020
# Reads file of steps per day. Then returns the average steps per day for each month
################################################################################

from calendar import *#import calendar module

months=month_name#list of month names
daysper=[31,28,31,30,31,30,31,31,30,31,30,31]#number of days in each month
step_list=[]#intialize step_list list
startindex=0#intialize start index
with open('steps.txt') as fo:#open file
    for lines in fo:#add each number in file to step list
        step_list.append(int(lines.rstrip()))

print('The average steps taken each month were:')#print header

for month in range(len(months)-1):#loop for each month
        numdays=daysper[month]#number of days for indexed month
        endindex=startindex+numdays#make end index equal to start index plus number of days in a month
        stepsper=sum(step_list[startindex:endindex])#sum the steps per month
        avg=stepsper/daysper[month]#find the average steps per day
        print(f'{months[month+1]:<10}:{avg:>7.1f}')#print the month and steps per day
        startindex=endindex#update start index as the current endindex
    
