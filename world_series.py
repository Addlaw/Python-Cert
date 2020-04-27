################################################################################
# Author: Addison Lawrence
# Date: 4/11/2020
# Allows a year to be input and returns the world series winner that
# year and how many times they have won
################################################################################

world_series={}#intialize dict
winners=[]#intialize list
index=0#intialize index

with open('WorldSeriesWinners.txt') as fo:#open text file
   for line in fo:
       winners.append(line.rstrip())#make a list of all world series winners
       
for x in range(1903,2020,1):#loop for each year
    if x==1904 or x==1994:#if during a year it was not played
        world_series[x]='not played'#set key value to not played
    else:#if was played then
        world_series[x]=winners[index]#set year value to the winner that year
        index+=1#update the index

year=int(input('Enter a year in the range 1903-2019: '))#ask user for year
winner=world_series.get(year)#get the winner that year

if winner==None:#if winner cannot be found
    print(f'Data for the year {year} is not included in the database.')
elif winner=='not played':#if during a year not played
    print(f"The world series wasn't played in the year {year}.")
else:#if valid winner
    wins=winners.count(winner)#count the number of winns they have had
    print(f'The {winner} won the World Series in {year}.')#print who won
    print(f'They have won the World Series {wins} times.')#print how much they have won
