################################################################################
# Author: Addison Lawrence
# Date: 3/22/2020
# Asks user to input 10 values then gives the max, min, total, and average of the list
################################################################################

index=1#intialize index variable
numberlist=[]#intialize list

while index<11:#while loop for 10 numbers
    message='Enter number '+str(format(index,'>2'))+' of 10: '#print message
    number=float(input(message))#number input
    numberlist.append(number)#add number to list
    index=index+1#update index
    
lowest=min(numberlist)#find lowest number in list
highest=max(numberlist)#find highest number in list
total=sum(numberlist)#find sum of the list
average=total/10#find the average of the list

print('Lowest number:',format(lowest,'.2f'))#print the lowest number in list
print('Highest number:',format(highest,'.2f'))#print the highest number in list
print('Total:',format(total,'.2f'))#print the sum of the list
print('Average:',format(average,'.2f'))#print the average of the list
