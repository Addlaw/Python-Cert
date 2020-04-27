################################################################################
# Author: Addison Lawrence
# Date: 2/22/2020
#Draws a spiral hexagon with 36 sides
################################################################################


from turtle import *#start turtle module

pensize(1)#makes the line 1 pixel wide
pendown#begin drawing
index=1#intialize index
while index<37:
    forward(index*5)#increase length of the side each time
    left(60)#turn the cursor 60 degree to the left
    index=index+1#increases index
done()
