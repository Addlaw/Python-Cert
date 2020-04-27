################################################################################
# Author: Addison Lawrence
# Date: 4/19/2020
# Asks user for sales input for each month then makes a pie chart out of the values
################################################################################

import matplotlib.pyplot as plt#import matplotlib
import calendar as c#import calendar module

months=c.month_name[1:13]#get month names from calendar
clrs=['#4D4038','#BAA892','#5B6870','#6E99B4','#A3D6D7','#085C11','#849E2A',
        '#C3BE0B','#E9E45B','#6B4536','#B46012','#FF9B1A']#list of colors for the chart
sales=[]#intialize sales list
for month in months:#for each month
    message='Enter the sales value of '+month+': '#update message for each month
    sale=int(input(message))#ask user for sales of that month
    sales.append(sale)#add sale to list

fig, monthlysales=plt.subplots()#begin figure plot
monthlysales.pie(sales, colors=clrs, labels=months)#make pie chart of sales and month
plt.show()#display plot





