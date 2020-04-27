################################################################################
# Author: Addison Lawrence
# Date: 2/4/2020
# Determines the color of a roulette pocket then displays it
################################################################################

#Asks user to input the pocket number
pocket=int(input('Please enter a pocket number: '))

#elif structure to determine the color of the pocket and then display it
#%2==0 finds the even numbers while %2==1 finds the odd numbers
if pocket==0:
    print('  Pocket',pocket,'is green.')
#0-10
elif (pocket>0 and pocket<=10)and pocket%2==0 :
    print('  Pocket',pocket,'is black.')
elif (pocket>0 and pocket<=10)and pocket%2==1:
    print('  Pocket',pocket,'is red.')
#11-18
elif (pocket>=11 and pocket<=18)and pocket%2==0:
    print('  Pocket',pocket,'is red.')
elif (pocket>=11 and pocket<=18)and pocket%2==1:
    print('  Pocket',pocket,'is black.')
#19-28
elif (pocket>=19 and pocket<=28)and pocket%2==0:
    print('  Pocket',pocket,'is black.')
elif (pocket>=19 and pocket<=28)and pocket%2==1:
    print('  Pocket',pocket,'is red.')
#29-36
elif (pocket>=29 and pocket<=36)and pocket%2==0:
    print('  Pocket',pocket,'is red.')
elif (pocket>=29 and pocket<=36)and pocket%2==1:
    print('  Pocket',pocket,'is black.')
#if none than the input is invalid
else:
    print('  Invalid Input!')










