################################################################################
# Author: Addison Lawrence
# Date: 4/23/2020
# Creates a bar graph of the letter frequency in the wheel of forture phrases document
################################################################################

import matplotlib.pyplot as plt#import matplotlib as plt

phraselist=[]#intialize phrase list
letter_list=[]#intialize letter list
letter_freq=[]#intialize letter frequency list
letters=0#intialize letter count

with open('phrases.txt') as fo:#open phrase.txt file
    for line in fo:#for each file line
        phraselist.append(line.rstrip())#add phrase to phraase list

for phrase in phraselist:#for each phrase in the list
    phrase=phrase.upper()#capitalize the phrase
    for character in phrase:#for each character in the list
        if character.isalpha()==True:#if character is a letter
            letter_list.append(character)#add character to letter list
            letters+=1#increase letter count by 1

letterset=sorted(set(letter_list))#make a set of all the letters and sort the set

for letter in letterset:#for each letter in the set
    num_of_let=letter_list.count(letter)#count the number of times the letter is in the list
    letter_freq.append(num_of_let/letters)#divide count of letter by total letters then append the frequency

letters_sort=list(letterset)#turn the letter set into a list

fig, wof=plt.subplots()#intialize plot
wof.bar(letters_sort,letter_freq)#make a bar graph of data
wof.set_title('Letter Frequency in Puzzle Phrases')#set title
wof.set_xlabel('Letter')#set x title
wof.set_ylabel('Letter Apperance Frequency')#set y title
wof.grid()#show grid
plt.show()#show plot
            
