################################################################################
# Author: Addison Lawrence
# Date: 2/4/2020
# This program determines wether or not a year is a leap year and then displays
# how many days are in the month.
################################################################################


year=int(input('Please input a year: '))

if (year%400==0 and year%100==0):
    print('In the year',year,', Febuary has 29 days.')
elif  (year%100 and year%4==0):
    print('In the year',year,', Febuary has 29 days.')
else:
    print('In the year',year,', Febuary has 28 days.')




