################################################################################
# Author: Addison Lawrence
# Date: 2/17/2020
# Finds the prime numbers up to a given input
################################################################################

def is_prime(number): 
    if number>=2:#makes sure the number is positive and greater than 1
        for numbers in range(2,number//2+1):#makes a list to divide the entered number by
            if(number%numbers==0):#determines if the number can be divided by anything
                return False#if yes returns false
        return True#if not divisable then returns true
    else:
        return False#if not in valid range for primes returns false



limit=int(input('Enter a positive integer: '))#input number for the top limit
message='The primes up to '+str(limit)+' are: '#start a message to print later
for number in range(0,limit+1):#for loop to make values to put in is_prime
    if is_prime(number):#runs the function and determines if numbers are prime
        message +=str(number)#add text to message string if is prime
        if number!=limit:
            message+=', '
print(message)#print while message
