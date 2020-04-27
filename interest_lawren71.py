##############################################################################
#Author:Addison Lawrence
#Date:1/28/20
#Caculates interest on a specified amount of investment.
##############################################################################

#ask user to enter quantities
print("Please enter the following quantities.")

#Asks for user to input intial amount, rate, times compounded per year, and years to mature
intial_value=float(input("How much is the intial deposit? "))
ratepercent=float(input("What is the annual interest rate in percent? "))
compounds_per_year=int(input("How many times per year is the interest compounded? "))
years=float(input("How many years will the account be left to earn interest? "))

rate=ratepercent/100#converts ratepercentage to a decimal rate number

#caculates the future value of the account
future_value=intial_value*((1+(rate/compounds_per_year))**(compounds_per_year*years))

#print final answer for user and format answer
print("At the end of",years,"years the account will be worth $",format(future_value,',.2f'))
