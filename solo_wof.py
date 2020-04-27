################################################################################
# Author: Addison Lawrence
# Date: 4/23/2020
# Allows the user to play a 4 round solo game of wheel of fortune.
# User defined functions on top. Program at the bottom.
################################################################################

import random as r#import the random module

#-------------------------------------------------------------------------------#

                          ##############################
                          #        Option 1 Spin       #
                          ##############################

#-------------------------------------------------------------------------------#

                            
def spinwheel(r_earnings,phrase,cons,clue):#definition line

    wheel=[500,500,500,500,500,550,600,600,600,600,650,650,650,
           700,700,700,800,900,2500,'BANKRUPT','BANKRUPT']#wheel values
    spin=r.choice(wheel)#choose a random value from the wheel
    
    if spin=='BANKRUPT':#If bankrupt is chooses
        print(f'The wheel landed on {spin}.\nYou lost ${r_earnings:,}!')#print spin value and earnings lost
        r_earnings=0#set round earnings to 0
        
    else:#if bankrup is not choosen
        print(f'The wheel landed on ${spin:,}.')#print the spin value
        letter,cons=getcons(cons)#use function to get a letter and update usable consonants
        clue=updateclue(letter,clue,phrase)#use update clue function to update clue
        letcount=phrase.count(letter)#count occurances of letter in phrase

        if letcount==0:#if not used anywhere
            print(f"I'm sorry, there are no {letter}'s.")#print sorry message
            
        elif letcount==1:#if used once
            profit=int(spin)*letcount#calculate the profit
            print(f"There is {letcount} {letter}, which earns you ${profit:,}.")#print number of letter occurances with "is" and without "'s"
            r_earnings+=profit#update the earnings for the round
            
        else:#if used more than once
            profit=int(spin)*letcount#calculate the profit
            print(f"There are {letcount} {letter}'s, which earns you ${profit:,}.")#print number of letter occurances with "are" and with "'s"
            r_earnings+=profit#update the earnings for the round
            
    return r_earnings,clue,cons#return the updates clue consonants list and round earnings

#-------------------------------------------------------------------------------#


def getcons(cons):#function definition line

    letter=input('Pick a consonant: ')#prompt user to input a consonant
    letter=letter.upper()#make sure the input is capitalized(case insensitivity)

    while letter not in cons:#if letter is not in the consonants list

        if len(letter)!=1:#if the input is longer than 1 character
            print('Please enter exactly one character.')#ask for only 1 character

        elif letter in vowelstup:#if the letter is a vowel
            print('Vowels must be purchased.')#tell user vowels must be purchased

        elif letter.isalpha()== False:#if character is not a letter
            print(f'The character {letter} is not a letter.')#print character and say it is not a letter

        elif letter not in cons:#if it is a consonant but not in the list
            print(f'The letter {letter} has already been used.')#tell user letter has been used

        letter=input('Pick a consonant: ')#prompt for a new input
        letter=letter.upper()#capitalize input
        
    index=cons.index(letter)#find each index of the letter
    cons[index]=' '#replace the consonant with a space
    return letter,cons#return consonant give and updated consonant list

#-------------------------------------------------------------------------------#

                        ##################################
                        #       Option 2 Buy Vowel       #
                        ##################################

#-------------------------------------------------------------------------------#
                            
def buyvowel(phrase,vowels,clue):#function definition line
    
    buy=str(input('Pick a vowel: '))#prompt user to input vowel
    buy=buy.upper()#capitalize input
    
    while buy not in vowels:#if input is not available
        
        if len(buy)!=1:#if more than one character input
            print('Please enter exactly one character.')
            
        elif buy.isalpha()== False:#if input is not a letter
            print(f'The character {buy} is not a letter.')
            
        elif buy in constup:#if input is a consonant
            print('Consonants cannot be purchased.')
            
        elif buy not in vowels:#if is vowel but not in vowels
            print(f'The letter {buy} has already been  purchased.')
            
        buy=str(input('Pick a vowel: '))##ask user for input
        buy=buy.upper()#capitalize input
        
    vowcount=phrase.count(buy)#Count number of vowel occurances
    
    if vowcount==0:#if none of that vowel
        print(f"I'm sorry there are no {buy}'s")
        
    elif vowcount==1:#if one of that vowel
        print(f"There is {vowcount} {buy}.")
        
    else:#if more than one of that vowel
        print(f"There are {vowcount} {buy}'s.")
        
    clue=updateclue(buy,clue,phrase)#update clue
    index=vowels.index(buy)#index vowel
    vowels[index]=' '#replace vowel with empty space
    return clue#return the updates clue
    
def updateclue(letter,clue,phrase):#function call to update clue
    
    letter_index=[]#intialize letter index

    for character in range(len(phrase)):#iterate through phrase
        if phrase[character]==letter:#check if the letter is at index
            letter_index.append(character)#add letter index to index list
            
    for index in letter_index:#for each index
        clue[index]=letter#update the cule with letter at indicies
    return clue#return updates clue

#-------------------------------------------------------------------------------#

                            ##########################
                            #        Option 3        #
                            ##########################
                            
#-------------------------------------------------------------------------------#
                   
def finishphrase(phrase,clue):#finishphrase difinition line
    
    print(f'Enter your solution.\n  Clues: {"".join(clue)}')#print clue
    guess=str(input('  Guess: '))#prompt for the phrase
    guess=guess.upper()#capitalize input (case insensitive)
    
    if guess==phrase:#if the guess is the phrase
        return 1#return 1
    
    else:#if wrong
        return 2#return 2

#-------------------------------------------------------------------------------#

                            ##########################
                            #       While loop       #
                            ##########################

#-------------------------------------------------------------------------------#

def validate_option(option):#validate option function definition line
    
    if option in ['1','2','3','4']:#if input is valid
        return int(option)#return input and end check
    
    else:#if not valid
        while option not in['1','2','3','4']:#ehile not valid
            print(f'{option} is an invalid choice.\nWhat would you like to do?')
            print(f'  1 - Spin the wheel\n  2 - Buy a vowel\n  3 - Solve the puzzel\n  4 - Quit the game') 
            option=input('Enter the number of your choice: ')#prompt for new input
        return int(option)#retun final valid input

    

################################################################################
#                                   Program                                    #
################################################################################

phraselist=[]#intialize phrase list
rounds=[1,2,3,4]#intialize rounds
total_earnings=0#intialize total earnings
solve_profit=[1000,0]#intialize solve profit

with open('phrases.txt') as fo:#open phrase.txt file
    for line in fo:#for each file line
        phraselist.append(line.rstrip())#add phrase to phraase list
    
for roundnum in rounds:#for each round
    solve=0#reset solve to 0
    r_earnings=0#reset round earnings to 0
    cons=['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']#consonants list
    constup=('B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z')#consonants tuple
    vowels=['A','E','I','O','U']#vowels list
    vowelstup=('A','E','I','O','U')#vowels tuple
    clue=[]#reset clue
    phrase=phraselist.pop(r.choice(range(0,len(phraselist))))#choose a random phrase and remove from list
    phrase=phrase.upper()#capitalize phrase
    
    for character in phrase:#for each character in the phrase
        if character.isalpha():#if character is a letter
            clue.append('_')#add a '_' to the clue
        else:#if not a letter
            clue.append(character)#add character to clue
            
    while solve==0:#while the solve status is 0
        r_earnings_str='$'+str("{:,}".format(r_earnings))#format round earnings for print statement
        print(f':::::::::::::::::::::::::::::::::::::::::: ROUND {roundnum} of 4 ::')#print round of
        print(f':: {"".join(clue):^52} ::')#print clue
        print(f'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')#spacer
        print(f':: {"".join(cons):^25} :: {"".join(vowels):^9} :: {r_earnings_str:>10} ::')#print avaliable letters and round esrnings
        print(f'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')#spacer
        print('What would you like to do?')
        print(f'  1 - Spin the wheel\n  2 - Buy a vowel\n  3 - Solve the puzzel\n  4 - Quit the game')#player options
        option=input('Enter the number of your choice: ')#prompt user to choose option
        option=validate_option(option)#validate option
        
        if option==1:#if option 1 chosen (spin wheel)
            if cons.count(' ')==len(cons):#if there are no consonants left 
                print('There are no more consonants to choose.')
            else:#if there are consonants left
                r_earnings,clue,cons=spinwheel(r_earnings,phrase,cons,clue)#call spinwheel function

        elif option==2:#if option 2 chosen (buy vowel)
            if vowels.count(' ')==len(vowels):#if there are no vowels left
                print('Thrre are no more vowels to buy.')
            elif r_earnings<250:#if round earnings are less than 250
                print(f'You need at least $250 to buy a vowel.')
            else:#is player can buy vowel
                r_earnings-=250#take 250 from player
                clue=buyvowel(phrase,vowels,clue)#run buy vowel function

        elif option==3:#if option 3 chosen (solve puzzle) (will end while loop)
            solve=finishphrase(phrase,clue)#run solve function (solve=1 solve correct)(solve=2 solve incorrect)

        elif option==4:#if option 3 chosen (quit game)
            solve=3#phrase unsolved end game (while loop)
        
    if solve==1:# if solve is 1 (correct solve)
        print('Ladies and gentlemen, we have a winner!')#print winner
        solve_profit[1]=r_earnings#put round earnings into solve profit
        r_earnings=max(solve_profit)#choose the biggest number
        total_earnings+=r_earnings#add round earnings to total earnings
        
    elif solve==2:# if solve is 2 (incorrect solve)
        print(f"I'm sorry. The correct solution was:\n{phrase}")#print sorry dont update total earnings
        
    elif solve==3:#if solve is 3 (player chose quit)
        total_earnings+=r_earnings#update total earnings with current round earnings
        print(f'You earned ${r_earnings:,} this round.')#print round earnings
        break#end the for loop
    
    print(f'You earned ${r_earnings:,} this round.')#print round earnings
    #end of for loop
print(f'Thanks for playing!\nYou earned a total of ${total_earnings:,}')#print total earnings
    
