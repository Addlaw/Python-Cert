################################################################################
# Author: Addison Lawrence
# Date: 3/22/2020
# sorts a list of numbers into a new list that are greater than a number
################################################################################

def main():#main function
    numberlist=[19,2940,10,24,29,1,85,201,-15,-122,799]#intial list
    number=13#number
    larger(number,numberlist)#function call

def larger(number,numberlist):#seperation function
    index=0#index intialize
    resultmatrix=[]#intialize result list
    for x in range(len(numberlist)):#for loop for list length
        inques=numberlist[x]#number in queestion
        if inques>number:#if number bigger than
            resultmatrix.append(inques)#add number to result matirx
    print('Number:',number)#print number
    print('List of numbers:\n',numberlist,sep='')#print original list
    print('Numbers in list that are greater than ',number,'\n',resultmatrix,sep='')#print final list

main()#main function call
