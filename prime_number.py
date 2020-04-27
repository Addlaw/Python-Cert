################################################################################
# Author: Addison Lawrence
# Date: 2/17/2020
# Determines wether or not an input is prime
################################################################################


def is_prime(number): 
    if number>=2:#makes sure the number is positive and greater than 1
        for numbers in range(2,number//2+1):#makes a list to divide the entered number by
            if(number%numbers==0):#determines if the number can be divided by anything
                return bool(0)#if yes returns false
        return bool(1)#if not divisable then returns true
    else:
        return bool(0)#if not in valid range for primes returns false





number=int(input('Enter a positive integer (-1 quit): '))#ask user to input a number
while number>=0:#while loop to continue until specified
    status=is_prime(number)#puts inumber into function and returns value to status
    if status==True:#uses status to determine the print statement
        print(number,'is prime number.')
    elif status==False:
        print(number,'is not prime number.')
    number=int(input('Enter a positive integer (-1 quit): '))#enter next number
