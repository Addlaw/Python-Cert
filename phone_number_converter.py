################################################################################
# Author: Addison Lawrence
# Date: 4/3/2020
# Turns a phone number with number and letters in to a completely numberical phone number
################################################################################

number=input('Enter a telephone number: ')#ask for user input
numnum=''#intialize string
for character in number:#for loop to convert number
    if character in ['0','1','2','3','4','5','6','7','8','9','-']:
        numnum+=character#if number then add the umber to the final sting
    #if a certain letter than add that number to the final number
    elif character in ['A','a','B','b','C','c']:
        numnum+='2'
    elif character in ['D','d','E','e','F','f']:
        numnum+='3'
    elif character in ['G','g','H','h','I','i']:
        numnum+='4'
    elif character in ['J','j','K','k','L','l']:
        numnum+='5'
    elif character in ['M','m','N','n','O','o']:
        numnum+='6'
    elif character in ['P','p','Q','q','R','r','S','s']:
        numnum+='7'
    elif character in ['T','t','U','u','V','v']:
        numnum+='8'
    elif character in ['W','w','X','x','Y','y','Z','z']:
        numnum+='9'
        
print('The phone number is',numnum)#print the converted number

