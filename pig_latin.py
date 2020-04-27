################################################################################
# Author: Addison Lawrence
# Date: 4/3/2020
# Converts a sentence into piglatin
################################################################################

sentence=str(input('Enter a string: '))#ask for user input
sensplit=sentence.split()#split the sentence into words
numwords=len(sensplit)#counts the number of words
piglatin=''#intialize the final string

for x in range(0,numwords):#for loop for each word in the sentence
    word=sensplit[x]#take one word from the list
    firstletter=word[0]#get the fist letter of the word
    resword=word[1:]#rest of the word
    word=resword+firstletter+'ay'#put the word together in pig latin and add ay
    piglatin+=word+' '#add word to the final message
    
print(piglatin.capitalize())#print sentence in pig latin and capitalize the fitst letter
