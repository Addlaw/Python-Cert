#grandpa program
#round barrn program
#finds radius for amount of panels used +1 for door
#uses 3 foot steel pieces
panels=float(input('Input number of panels '))
pi=3.14159265359
num_sides=panels+1
circumference=num_sides*3
radius=circumference/(pi*2)
angle_between=360/num_sides
print('angle between panels',format(angle_between,'.4f'),'(inner angle)')
print('radius is',format(radius,'.4f'),'feet')
