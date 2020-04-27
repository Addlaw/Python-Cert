################################################################################
# Author: Addison Lawrence
# Date: 3/2/2020
# Draws all vowels out in a random order
################################################################################

import random as r#import random with r call
from vowels_aclawrence import *#import vowels to draw letters
List=[a,e,i,o,u]#create list of possible vowels
loop=0#intialize loop
choice=r.sample(List,5)#make a list where random choses each vowel once
pensize(5)#set pen size
while loop<5:#set number of iterations
    penup()#stop drawing
    setheading(0)#point turtle to 0
    goto((60*loop)-120,0)#move turtle start each iteration
    choice[loop]()#refercences random list and uses function to draw vowels
    loop=loop+1#update loop

    
