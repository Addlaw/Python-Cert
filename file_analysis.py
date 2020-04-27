###############################################################################
# Author: Addison Lawrence
# Date: 4/11/2020
# Reads two text files then makes a new text file of words used and number of times
# they have been used for each doc. Then makes a doc of words used in both docs and
# and one of words only used in one doc.
################################################################################


def wordvals(file):#user defined function
    wordict={}#intialize dict
    words=[]#intialize list
    with open(file) as fo:#open txt file
        everything=fo.read()#read the doc
    words=everything.lower().split()#split all the words up
    #strip all unwanted characters
    wordsfinal=[word.strip('.').strip('"').strip('!').strip(',').strip('(').strip(')') for word in words]
    wordsfinal.sort()#sort the list
    for word in wordsfinal:#for loop to create dict from the list
        if wordict.get(word)==None:#if no dict exists
            wordict[word]=1#add dict to dict
        else:#if dict exists
            wordict[word]+=1#increase dict value   
    return wordict#return the dict
           

t1dict=wordvals('xian_1.txt')#run function with file 1 to get a dict
with open('xian_1_word_frequency.txt','a') as fo:#Create file to write too
    for key in t1dict:#for each dict value
        fo.write(key+':'+str(t1dict.get(key))+'\n')#write word and tiems used
        
t2dict=wordvals('xian_2.txt')#run function with file 2 to get a dict
with open('xian_2_word_frequency.txt','a') as fo:#Create file to write too
    for key in t2dict:#for each dict value
        fo.write(key+':'+str(t2dict.get(key))+'\n')#write word and tiems used


t1set=set(t1dict)#make a set from file 1 dict
t2set=set(t2dict)#make a set from file 1 dict
common=t1set & t2set#find the common words from both files
common=sorted(common)#sort common set
exclusive=t1set ^ t2set#find the words exclusive to each file
exclusive=sorted(exclusive)#sort the exclusive set

with open('common_words.txt','a') as fo:#Create file to write too
    for word in common:#for each value in the set
        fo.write(word+'\n')#write the word to the file
        
with open('eitherbutnotboth.txt','a') as fo:#Create file to write too
    for word in exclusive:#for each value in the set
        fo.write(word+'\n')#write the word to the file








