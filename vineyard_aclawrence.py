##############################################################################
#Author:Addison Lawrence
#Date:1/29/20
#Caculates the number of grape vines that can be planted in an area with certain specifications.
##############################################################################

#Ask user to enter quantities
print("Enter the following quantities in feet.")

#Ask user to input values for length of row, end post assembly, and space between vines
row_length=float(input("  How long is this row? "))
end_post=float(input("  How wide is the end-post assembly? "))
space=float(input("  How much space should be between the vines? "))

#calculate the number of vines that can be planted
num_of_vines=((row_length-(2*end_post))/space)

#print the number of vines that can be planted
print("\nThis row has enough space for",format(int(num_of_vines),'.0f'),"vine(s)")
