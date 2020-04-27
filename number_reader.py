################################################################################
# Author: Addison Lawrence
# Date: 4/3/2020
# Finds the min,max,sum, and average of numbers in a text file
################################################################################

numbers=[]#intializes number list
with open('random_numbers.txt') as fo:#opens file
    #adds each number in the file to the number list
    for number in fo:
        numbers.append(int(number.rstrip()))

numofnums=len(numbers)
num_max=max(numbers)#finds the max of the numbers
num_min=min(numbers)#finds the minimum of the numbers
num_sum=sum(numbers)#sums the number list
num_avg=num_sum/len(numbers)#finds the average of the numbers
#prints the max,min,sum, and average
print(f'{numofnums:,} numnbers were read from the file.')#print amount of numbers read
print(f'Max: {num_max}\nMin: {num_min}\nSum: {num_sum:,}\nAvg: {num_avg:.1f}')#print min,max,sum, and average
