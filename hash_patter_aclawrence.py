################################################################################
# Author: Addison Lawrence
# Date: 2/12/2020
# Creates a triangular has pattern for number of lines given by increasing space
# between hashes
################################################################################


lines=int(input('Enter the number of lines: '))#ask user to input number of lines

#For loop to create the pattern
for row in range(lines):
    print('#',end='',sep='')#print first hash
    for spaces in range(row):
        print(' ',end='',sep='')#print spaces
    print('#',sep='')#print end hash
