################################################################################
# Author: Addison Lawrence
# Date: 2/12/2020
# Calculates the population of an organism when given percentage increase, staring number,
# and number of dys to populate
################################################################################

#asks user to input the intial population, percent increase,
#and the number of days they are allowed to multiply
population=int(input('Starting Number of organisms: '))
increase=float(input('Average daily increase, in percent: '))
days=float(input('Number of days to miltiply: '))

print('Day     Approx. Pop')#prints the header
percentage=increase/100#converts the percent to the actual decimal
day=0#intializes the day value
#while loop
while days>0:
    day=day+1#update the day variable
    print('',format(day,'<2d'),'      ',format(population,'>8.4f'))#print values
    population=population*(1+percentage)#calculate the population
    days=days-1#reduce the days index
