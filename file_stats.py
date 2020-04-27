################################################################################
# Author: Addison Lawrence
# Date: 4/3/2020
# Opens a file and gives the number of words, lines, and average words per line
################################################################################

with open('rumpelstiltskin.txt') as fo:#open the text file
    contents=fo.read()#read the contents
lines=contents.count('\n')#count the number of lines in the text
words=len(contents.split())#count the number of words
average=words/lines#calculate the average words per line

#print the number of words and lines
print(f'Total number of words: {words}\nTotal number of lines: {lines}')
#print the average words per line
print(f'Average number of words per line: {average:.1f}')
