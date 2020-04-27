################################################################################
# Author: Addison Lawrence
# Date: 2/12/2020
# Calculates the total and monthly average rain fall when given values
################################################################################

years=int(input('Enter number of years: '))#asks user to input amount of time

#intializes year and total variables
year=0
total=0

months=years*12#calculats months from years

#while loop
while years>0:
    year=year+1#year update
    print('For year No.',year,sep='')#prints which year data is entered for
    #input statements for each month (repeated for each year)
    total+=float(input('Enter rainfall amount for Jan.: '))
    total+=float(input('Enter rainfall amount for Feb.: '))
    total+=float(input('Enter rainfall amount for Mar.: '))
    total+=float(input('Enter rainfall amount for Apr.: '))
    total+=float(input('Enter rainfall amount for May.: '))
    total+=float(input('Enter rainfall amount for Jun.: '))
    total+=float(input('Enter rainfall amount for Jul.: '))
    total+=float(input('Enter rainfall amount for Aug.: '))
    total+=float(input('Enter rainfall amount for Sep.: '))
    total+=float(input('Enter rainfall amount for Oct.: '))
    total+=float(input('Enter rainfall amount for Nov.: '))
    total+=float(input('Enter rainfall amount for Dec.: '))
    years=years-1#years variable update



average=total/months#monthly average calculation

#print statements for number of months, total rainfall, and monthly average
print('There are',months,'months.')
print('Tho total rainfall is',format(total,'.2f'),'inches.')
print('The monthly average rainfall is',format(average,'.2f'),'inches.')
    














##total=0
##total+=float(input('enter rain fall for jan'))
##total+=float(input('enter rain fall for feb'))
##total+=float(input('enter rain fall for mar'))
##total+=float(input('enter rain fall for apr'))
##total+=float(input('enter rain fall for may'))
##total+=float(input('enter rain fall for jun'))
##total+=float(input('enter rain fall for jul'))
##total+=float(input('enter rain fall for aug'))
##total+=float(input('enter rain fall for sep'))
##total+=float(input('enter rain fall for oct'))
##total+=float(input('enter rain fall for nov'))
##total+=float(input('enter rain fall for dec'))
