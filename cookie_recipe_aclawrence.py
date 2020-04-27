##############################################################################
#Author:Addison Lawrence
#Date:1/28/20
#Caculates ingredients needed to make a specified amount of cookies.
##############################################################################

#asks user to input amount of cookies
numofcookies=int(input("How many cookies do you want to make? "))

#calculation for sugar needed
sugarneeded=float((1.5/48)*numofcookies)
#calculation for butter needed
butterneeded=float((1/48)*numofcookies)
#calculation for flour needed
flourneeded=float((2.75/48)*numofcookies)

#print commands to display ingredients needed and format answers
print("To make",numofcookies," cookies, you will need:")  
print("  ",format(sugarneeded,'.2f'),"cups of sugar")  
print("  ",format(butterneeded,'.2f'),"cups pf butter") 
print("  ",format(flourneeded,'.2f'),"cups of flour")
