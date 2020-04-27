###############################################################################
# Author: Addison Lawrence
# Date: 4/11/2020
# Allows user to input a class and get the instructor,room, and class time back
################################################################################

#create the dict
courses={'CS101': {'Room':'3004', 'Instructor':'Haynes', 'Time':'8:00 a.m.'},
'CS102': {'Room':'4501', 'Instructor':'Alvarado', 'Time':'9:00 a.m.'},
'CS103': {'Room':'6755', 'Instructor':'Rich', 'Time':'10:00 a.m.'},
'NT110': {'Room':'1244', 'Instructor':'Burke', 'Time':'11:00 a.m.'},
'CM241': {'Room':'1411', 'Instructor':'Lee', 'Time':'1:00 a.m.'}}

course=str(input('Enter a course number: '))#ask user to input course
coursedict=courses.get(course)#get the course specific dict

if coursedict==None:#if invalid course
    print(f'{course} is an invalid course number.')#print invalid
else:#if valid course  
    print(f'The details for course {course} are:')#print header
    print('  Instructor:',courses[course]['Instructor'])#print instructor
    print('        Room:',courses[course]['Room'])#print room
    print('        Time:',courses[course]['Time'])#print time






