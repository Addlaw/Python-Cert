################################################################################
# Author: Addison Lawrence
# Date: 2/22/2020
#Writes hello turtle
################################################################################

from turtle import *#import the turtle module

def l():#function for letter l
    forward(25)#move to position
    pendown()#begins to trace
    left(90)#turn the turtle
    forward(100)#traces to position
    penup()#stops tracing
    
def t() :#function for letter t
    l()#uses function l
    left(135)#turn the turtle
    forward(35)#move to position
    left(135)#turn the turtle
    pendown()#begins to trace
    forward(50)#traces to position
    penup()#stops tracing
    
def o() :#function for letter o
    forward(25)#move to position
    pendown()#begins to trace
    circle(25)#traces circle
    penup()#stops tracing
    
def e():#function for letter e
    forward(35)#move to position
    circle(25,270)#move to position
    pendown()#begins to trace
    left(90)#turn the turtle
    forward(50)#traces to position
    left(90)#turn the turtle
    circle(25,315)#traces to position
    penup()#stops tracing
    
def h() :#function for letter h
    backward(25)#move to position
    l()#uses function l
    right(90)#turn the turtle
    forward(50)#move to position
    right(90)#turn the turtle
    forward(100)#move to position
    left(180)#turn the turtle
    pendown()#begins to trace
    forward(25)#traces to position
    circle(25,180)#traces to position
    penup()#stops tracing
    
def r() :#function for letter r
    forward(25)#move to position
    pendown()#begins to trace
    left(90)#turn the turtle
    forward(50)#move to position
    penup()#stops tracing
    left(90)#turn the turtle
    backward(25)#traces to position
    pendown()#begins to trace
    circle(25,90)#traces to position
    penup()#stops tracing
    
def u() :#function for letter u
    left(90)#turn the turtle
    forward(50)#move to position
    pendown()#begins to trace
    right(180)#turn the turtle
    forward(25)#traces to position
    circle(25,180)#traces to position
    forward(25)#traces to position
    right(180)#turn the turtle
    forward(50)#traces to position
    penup()#stops tracing

def main():#main function
    heigth=0#intializes y cordinate
    index=0#intializes index
    letters={'t':t, 'u':u, 'o':o, 'l':l, 'h':h, 'e':e, 'r':r}#intialize vector
    words="hello turtle"#words to write
    for counter, letter in enumerate(words):#enumerates the words given
        penup()#prevents pen from writing when moving to coordinates
        pensize(5)#defines pen size
        goto(index*60-150,heigth)#move the turtle to coordinates
        setheading(0)#set angle to 0
        if letter in letters:#if statement if letters are known
            letters[letter]()#reference the vector and then runs that function
            index=index+1#updates the index
        else:#if number is unknown updates the coordinates
            heigth=-125#makes the 
            index=0#reset the index to 0
            
main()#run the main function
done()#end the program
