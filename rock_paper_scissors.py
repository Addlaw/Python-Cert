################################################################################
# Author: Addison Lawrence
# Date: 2/29/2020
# Plays a game of rock paper scissors
################################################################################

def win(p,c):#determines if it is a tie and then sends values to the proper function
    if p==c:  
        return 'Its a tie.'
    elif p=='rock':
        return rock(p,c)
    elif p=='paper':
        return paper(p,c)
    elif p=='scissors':
        return scissors(p,c)

def rock(p,c):#player chooses rock decides wether or not the player wins
    if p=='rock' and c=='paper':
        return 'The computer won the game.'
    else:
        return 'You won the game.'
        
def paper(p,c):#player chooses paper decides wether or not the player wins
    if p=='paper' and c=='scissors':
        return 'The computer won the game.'
    else:
        return 'You won the game.'
        
def scissors(p,c):#player chooses scissors decides wether or not the player wins
    if p=='scissors' and c=='rock':
        return 'The computer won the game.'
    else:
        return 'You won the game.'
    
def validate(player,computer):#makes sure the player value is valid
    while player!='rock' and player!='paper' and player!='scissors':#makes sure player input is valid
        print('You made an invalid choice. Please try again.')
        #asks for new choice is player is invalid
        player=str(input('Enter rock, paper,scissors: '))
        computer=choice(['rock','paper','scissors'])
    return(player,computer)
        
from random import *#import random

player=str(input('Enter rock, paper,scissors: '))#player enter vlaue
computer=choice(['rock','paper','scissors'])#computer random choice

(player,computer)=validate(player,computer)#validate values

result=win(player,computer)#determin the intial result

while result=='Its a tie.':#if it is a tie then play again
    print('  The computer chose ',computer,',\n  and you chose ',player,'.',sep='')
    print('  ',result,' Starting over.\n',sep='')
    #ask for new answer, computer choose, validate,and determine new result
    player=str(input('Enter rock, paper,scissors: '))
    computer=choice(['rock','paper','scissors'])
    (player,computer)=validate(player,computer)
    result=win(player,computer)
print('  The computer chose ',computer,',\n  and you chose ',player,'.',sep='')
print(' ',result,'\nThanks for playing.')
