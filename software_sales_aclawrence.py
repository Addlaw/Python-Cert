################################################################################
# Author: Addison Lawrence
# Date: 2/4/2020
# Determnes and applies discount based on number of units purchased then displays
# answer
################################################################################

#possible discounts
applied_discount1=10
applied_discount2=25                  
applied_discount3=35
applied_discount4=45
#discount turned in to percent for the multiplication
nodiscount=1
discount1=(100-applied_discount1)/100
discount2=(100-applied_discount2)/100                  
discount3=(100-applied_discount3)/100
discount4=(100-applied_discount4)/100
#cost per unit ($)
Cost=99
#ask user to input number of units purchased
num_purchased=int(input('Please input the number of packages to be purchased: '))


#elif structure determining discount,applying it, and displaying final formated answer                  
if (num_purchased>0 and num_purchased<=9):#no discount
    print('  No discount applied.')
    total_cost=(Cost*num_purchased)*nodiscount
    print('  The final price for purchasing',num_purchased,'packages is $'\
          ,format(total_cost,',.2f'), sep='')
elif (num_purchased>=10 and num_purchased<=19):#discount 1
    print('  ',applied_discount1,'% discount applied.',sep='')
    total_cost=(Cost*num_purchased)*discount1
    print('  The final price for purchasing',num_purchased,'packages is $'\
          ,format(total_cost,',.2f'), sep='')            
elif (num_purchased>=20 and num_purchased<=49):#discount 2
    print('  ',applied_discount2,'% discount applied.',sep='')
    total_cost=(Cost*num_purchased)*discount2
    print('  The final price for purchasing',num_purchased,'packages is $'\
          ,format(total_cost,',.2f'), sep='')            
elif (num_purchased>=50 and num_purchased<=99):#discount 3
    print('  ',applied_discount3,'% discoint applied.',sep='')
    total_cost=(Cost*num_purchased)*discount3
    print('  The final price for purchasing',num_purchased,'packages is $'\
          ,format(total_cost,',.2f'), sep='')            
elif (num_purchased>=100):#discount 4
    print('  ',applied_discount4,'% discount applied.',sep='')
    total_cost=(Cost*num_purchased)*discount4
    print('  The final price for purchasing',num_purchased,'packages is $'\
          ,format(total_cost,',.2f'), sep='')            
elif (num_purchased<=0):#invalid
    print('  Invalid Input!')
