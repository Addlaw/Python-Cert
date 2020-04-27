################################################################################
# Author: Addison Lawrence
# Date: 4/19/2020
# Creates a bar chart or corona virus cases in Indiana 
################################################################################

import matplotlib.pyplot as plt#import matplotlib module
import datetime#import date time module

alldata=[]#intialize alldata list
date=[]#intialize date list
postest=[]#intialize postest list
totalpos=[]#intialize totalpos list

with open('corona_data.txt') as fo:#open corona file
    for lines in fo:
        alldata.append(lines.rstrip())#add each line to a list
        
for x in range(len(alldata)):#for each value
    worklist=alldata[x].split()#split the list
    y,m,d=worklist[0].split('-')#split the date in the list
    finaldate=datetime.date(int(y),int(m),int(d))#recompose the date
    date.append(finaldate)#add the date to the date list
    postest.append(int(worklist[2]))#add positive tests to a list
    totalpos.append(sum(postest))#sum the positive values to get a total


fig, corona=plt.subplots()#start plot figure
fig.autofmt_xdate()#auto format dates for x axis
corona.bar(date,totalpos,color='b')#create bar chart with date and total positive tests
corona.set_title('Positive COVID-19 Cases in Indiana')#plot title
corona.set_xlabel('Date')#x label
corona.set_ylabel('Number of Cases')#y label
corona.set_yticks([1000,2000,3000,4000,5000])#set ticks for y axis
plt.show()#show plot
