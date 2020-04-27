################################################################################
# Author: Addison Lawrence
# Date: 3/22/2020
# Runs through matricies to check if they are or are not Lo Shu magic squares.
# Then prints matrix and then says if it is or not
################################################################################


def numbercheck(matrix):
    num1s,num2s,num3s,num4s,num5s,num6s,num7s,num8s,num9s=0,0,0,0,0,0,0,0,0#intializes variables
    message1='It is not a Lo Shu Magic square'#return message
    for x in range(3):#for loop to run through rows
        row=matrix[x]#assign row to variable
        for column in range(3):#for loop to run through column
            number=row[column]#assign column to variable
            if number>9 or number<0:#checks if number is between 1 and 9
                return message1#returns message 1
            #adds numbers to variable and makes sure there is only 1 of each number
            elif number==1:
                num1s=num1s+1
                if num1s!=1:
                    return message1
            elif number==2:
                num2s=num2s+1
                if num2s!=1:
                    return message1
            elif number==3:
                num3s=num3s+1
                if num3s!=1:
                    return message1
            elif number==4:
                num4s=num4s+1
                if num4s!=1:
                    return message1
            elif number==5:
                num5s=num5s+1
                if num5s!=1:
                    return message1
            elif number==6:
                num6s=num6s+1
                if num6s!=1:
                    return message1
            elif number==7:
                num7s=num7s+1
                if num7s!=1:
                    return message1
            elif number==8:
                num8s=num8s+1
                if num8s!=1:
                    return message1
            elif number==9:
                num9s=num9s+1
                if num9s!=1:
                    return message1
            else:#if all are only one then passes check
                return 

            
def square_test(matrix):
    message1='It is not a Lo Shu Magic square'#return message 1
    message2='It is a Lo Shu Magic square'#return message 2
    rows=len(matrix)#counts rows in matrix
    columns=len(matrix[0])#counts columns in the rows
    line1=matrix[0]#assigns first list to row 1
    line2=matrix[1]#assigns second list to row 2
    line3=matrix[2]#assigns thrid list to row 3
    #size check
    if rows==3 or columns==3:#checks if rows and columns are equal to 3
        return message1
    #number check
    result=numbercheck(matrix)#runs the number check function
    if result==message1:#if a message is returned then the square fails
        return message1
    #row check
    for rowindex in range(3):#for loop for each list in the matrix
        line=matrix[rowindex]#assign a list in the matrix to line
        rowsum=sum(line)#sums the list
        if rowsum!=15:#check to make sure the sum is 15
            return message1#otherwise return message and end the function
            break
    #column check
    for column in range(3):#for loop for each column in the list
        columnsum=line1[column]+line2[column]+line3[column]#sum the columns
        if columnsum!=15:#check is the sum is 15
            return message1#other wise return message and end the function
            break
    #diagonal checks
    diag1sum=line1[0]+line2[1]+line3[2]#sum a diagonal
    if diag1sum!=15:#check if sum is 15
        return message1#other wise return message
    diag2sum=line1[2]+line2[1]+line3[0]#sum the other diagonal
    if diag2sum!=15:#check if sum is 15
        return message1#other wise return message
    return message2#if all checks are passed return message 2


def matrixprint(matrix):
    message=''#intialize message
    print('Your matrix is:')#print header
    for row in range(3):#for loop for rows
        line=matrix[row]#set matrix row to line
        for column in range(3):#index through columns
            message+=str(line[column])+' '#add number and space to message
            if column==2:#if the end of the for loop then print
                print(message)#print message
                message=''#reset message


def main():
    matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]#matrix 1
    matrix2=[[5, 5, 5], [5, 5, 5], [5, 5, 5]]#matrix 2
    matrix3=[[4, 9, 2], [3, 5, 7], [8, 1, 6]]#matrix 3
    result=square_test(matrix)#run function with matrix and get result
    matrixprint(matrix)#run print matrix
    print(f'{result}.\n')#print result
    result=square_test(matrix2)#run function with matrix and get result
    matrixprint(matrix2)#run print matrix
    print(f'{result}.\n')#print result
    result=square_test(matrix3)#run function with matrix and get result
    matrixprint(matrix3)#run print matrix
    print(f'{result}.\n')#print result
    
main()#run main function











        
