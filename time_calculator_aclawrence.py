################################################################################
# Author: Addison Lawrence
# Date: 2/4/2020
# Calculates the number of days,hours, or minutes that can be made out of a given
# number of seconds
################################################################################

#asks user to input number of seconds
num_sec=int(input('Please enter the time in seconds. '))

#elif structure to determine what the amount of seconds is
if num_sec<60:#makes sure the number of seconds is above 60
    print('  The number of seconds is less than one minute.')
elif num_sec%86400==0:#checks if time can be made in to perfect days
    days=num_sec//86400#makes time into days only
    print('  ',num_sec,'seconds is:',days,'day(s)')
elif num_sec%3600==0 and num_sec<86400:#checks if time can be made in to perfect hours
    hours=num_sec//3600#makes time in to hours only
    print('  ',num_sec,'seconds is:',hours,'hour(s)')
elif num_sec%60==0 and num_sec<3600:#checks if time can be made in to perfect minutes
    minutes=num_sec//60#makes time in to minutes only
    print('  ',num_sec,'seconds is:',minutes,'minute(s)')
elif num_sec>=60 and num_sec<3600:#checks if time is in minute to second range
    minutes=num_sec//60#calculates how many minutes can be made from seconds
    seconds=num_sec%60#finds the remaining seconds
    print('  ',num_sec,'seconds is:',minutes,'minute(s) and',seconds,'second(s)')
elif num_sec>3600 and num_sec<86400:#checks if time is in hour to second range
    hours=num_sec//3600#calculates how many hours can be made from seconds
    minutes=num_sec%3600#finds seconds left over from making hours
    minutes=minutes//60#calculates how many minutes can be created from remaining seconds
    seconds=num_sec%60#finds the remaining seconds
    print('  ',num_sec,'seconds is:',hours,'hour(s),',minutes,'minute(s) and',seconds,'second(s)')
elif num_sec>=86400:#checks if times is in day to second range
    days=num_sec//86400#calculates the perfect amount of days that can be made
    hours=num_sec%86400#finds seconds left over from making days
    hours=hours//3600#calculates how many hours can be made from remaining seconds
    minutes=num_sec%3600#finds seconds left over from making hours
    minutes=minutes//60#calculates how many minutes can be created from remaining seconds
    seconds=num_sec%60#finds the remaining seconds
    print('  ',num_sec,'seconds is:',days,'day(s),',hours,'hour(s),',minutes,\
          'minute(s) and',seconds,'second(s)')



