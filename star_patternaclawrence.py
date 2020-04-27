################################################################################
# Author: Addison Lawrence
# Date: 2/22/2020
#Makes a star with number of specified points
################################################################################


from turtle import *#imports the turtle module
color('black','pink')#makes the outline of the turtle black and the fill pink
pensize(5)#makes the pen size 5
pendown#puts the pen down
index=0#intializes index
points=int(input('input points: '))#asks for point input
begin_fill()#begin the shape fill
left(90-((360/points)/2))#turns the intial turtle
while index<points:#while loop to draw star
    left(180-(2*360/points))#turns the turtle for the outside angles
    forward(50)#turtle moves 50 pixles forward
    right(180-360/points)#turns the turtle for the inner angles
    forward(50)
    index=index+1#updates the index
end_fill()#fill the shape
done()
