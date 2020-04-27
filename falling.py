################################################################################
# Author: Addison Lawrence
# Date: 2/17/2020
# Calculates the distance an object has fallen when given the time it has fallen for.
################################################################################

def falling_distance(time):#function set up
    gravity=9.81#intialize the gravity constant
    distance=(gravity*time**2)/2#equation to calculate the distance fallen
    print(format(time,'>7d'),format(distance,'>14.2f'))#display calculated values


print('Time (s)  Distance (m) \n ---------------------')#print the column labeles
time=10#intialize the time variable
for seconds in range(1,time+1):#loop continues while the time is less than the input time
    falling_distance(seconds)#input the time into the function
    
