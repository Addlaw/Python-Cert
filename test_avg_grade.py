################################################################################
# Author: Addison Lawrence
# Date: 2/17/2020
# Asks user to enter grades then returns the letter grade and calculates the average grade
################################################################################


def get_valid_score():
    score=float(input('Enter a score: '))#asks user to input a score
    if score<0 or score>100:#determines if score is in rance
        return print('Invalid Input. Please try again.')
    else:
        return score#returns score if valid

def calc_average(scores):
    number_scores=len(scores)#counts the number of scores entered
    score_total=sum(scores)#sums all the scores
    average=score_total/number_scores#calculates the average of the scores
    return average#returns the average

def determine_grade(score):#determines the grade given for the score input
    if score<60:
        return str('F')
    elif score<70:
        return str('D')
    elif score<80:
        return str('C')
    elif score<90:
        return str('B')
    else:
        return str('A')



scores=[]#preallocates the scores index
while len(scores)<5:#while loop for 5 valid scores
    score=get_valid_score()#calls valid score function
    if score!=None:#if a score is returned executs the rest of the program
        grade=determine_grade(score)#inputs the score into the grade function
        scores.append(score)#adds the score to a list
        print('The letter grade for',format(score,'.1f'),'is',grade,end='.\n')
    else:
        scores=scores#if a non valid score is entered the scores array is unchanged
average=calc_average(scores)#after all scores have been entered runs average function
print('The average test score is',format(average,'.2f'))


    
