################################################################################
# Author: Addison Lawrence
# Date: 2/4/2020
# Calculates the Reynold's number for for a pipe when given certain inputs
################################################################################

#asks user to in put velocity, pipe diameter, and temperature
velocity=float(input("Enter the velocity of water in the pipe: "))
diameter=float(input("Enter the pipe's diameter: "))
temperature=float(input("Enter the temperature in \u00B0C as 5, 10, or 15: "))

#determines the viscosity value based on entered variables
if temperature==5:
    viscosity=.00000149
elif temperature==10:
    viscosity=.00000131
elif temperature==15:
    viscosity=.00000115

#calculates the Reynold's number
reynolds_num=((velocity*diameter)/viscosity)

#prints all information
print("The Reynolds number for flow at ",velocity," m/s in a "\
      ,diameter," m diameter pipe at ",temperature,"\u00B0C is "\
      ,format(reynolds_num,'.2e'),".",sep="")
