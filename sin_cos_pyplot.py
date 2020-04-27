################################################################################
# Author: Addison Lawrence
# Date: 4/19/2020
# Graphs sine and cosine  
################################################################################

import matplotlib.pyplot as plt#import matplotlib module
from math import sin,cos,pi#import math operations


ticks=200#number of values from 1-2pi
xes=[]#intialize list for x's
cosine=[]#intialize cosine list
sine=[]#intialize sine list
for tick in range(ticks+1):
    x=2*pi*tick/ticks#calculate x value
    xes.append(x)#add x to xes list
    cosine.append(cos(x))#add cosine value to cosine list
    sine.append(sin(x))#add sine value to sine list


fig, trig=plt.subplots()#begin creating plot
trig.plot(xes,cosine,color='b')#plot cosine values as blue
trig.plot(xes,sine,color='r')#plot sine values as red
trig.set_yticks([-1,1])#set y tick marks
trig.set_xticks([pi/2,pi,(3*pi)/2,2*pi])#set the x tick marks
trig.set_xticklabels(['$\pi/2$','$\pi$','$3\pi/2$','$2\pi$'])#x axis labels
trig.spines['bottom'].set_position('zero')#set bottom spline to origin
trig.spines['left'].set_position('zero')#set left spline to origin
trig.spines['top'].set_visible(False)#remove top spline
trig.spines['right'].set_visible(False)#remove right spline
plt.show()#show plot
