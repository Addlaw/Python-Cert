################################################################################
# Author: Addison Lawrence
# Date: 3/9/2020
# Makes a graph and graphs sine and cosine from 0 to 2pi
################################################################################

from math import*
from turtle import*

def tick_mark():#mkae the tick marks
    pendown()
    forward(10)
    penup()

def stamps():#put arrows at the end of the praph lines
    penup()
    forward(5)
    stamp()

#set up the graph
pensize(5)
turtlesize(2)
penup()
goto(-100,0)
pendown()
forward(pi*100+50)
stamps()
goto(-75,-60)
left(90)
pendown()
forward(130)
stamps()
hideturtle()
for tick in range(0,4):#makes the vertical tick marks
    x_val=50*tick*(pi/2)
    goto(x_val,0)
    setheading(90)
    tick_mark()
goto(-75,-50)
setheading(0)
tick_mark()
goto(-75,50)
setheading(0)
tick_mark()
pensize(3)
pendown()

color('blue')
for x in range(0,361*2):#graph the cosine graph
    x_val=(50*(x*pi)/360)-75
    y_val=50*cos((x*pi)/360)
    goto(x_val,y_val)
#reset the turtle to the graph origin
penup()
goto(-75,0)
pendown()
color('red')

for x in range(0,361*2):#graph the sin graph
    x_val=(50*(x*pi)/360)-75
    y_val=50*sin((x*pi)/360)
    goto(x_val,y_val)
done()
