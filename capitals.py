################################################################################
# Author: Addison Lawrence
# Date: 4/11/2020
# Makes a quiz of 50 state's capitals
################################################################################


from random import *#import random module

state_cap={}#intialize dict
with open('state_capitals.txt') as fo:#open txt file
   for line in fo:
       statecap=line.strip()#take line from file
       capital, state = statecap.split(', ')#split line into state and capital
       state_cap[state]=capital#make a dict out of values

correct=0#intialize number of correct
total=0#intialize the total
answer=1#set answer value (just to run the loop)
while answer!=0:#while answer is not 0 loop
    state=choice(list(state_cap.keys()))#state is a random choice from the dict
    capital=state_cap.get(state)#capital is the value for the state key
    guess=input(f'What is the capital of {state}? (enter 0 to quit): ')#user input/guess
    if guess==capital:#check if the guess is correct
        correct+=1#update correct value if correct
        total+=1#update the total
        print('That is correct')#print correct
    elif guess=='0':#if guess is zero
        answer=0#set answer to 0 to stop loop
        print(f'You answered {correct} out of {total} questions correctly.')#print final score
    elif guess!=capital:#if guess is wrong
        total+=1#update the total
        print(f'That is incorrect.\nThe capital of {state} is {capital}')#print incorrect then correct answer
        
