# This program defines two functions - calc_average & determine_grade.
# The main function controls program flow and calls both the calc_average and
# determine_grade functions. The calc_average function accepts 5 test scores as arguments
# and returns the average of the scores to the main function. The determine_grade
# function accepts a test score as an argument and returns a letter grade for the score
# to the main function. The program will display a letter grade for eacg test score
# and the average of the 5 test scores.
# 
# 11/12/17
# CTI-110 M6HW1 - Test Average and Grade
# Timothy Novak
# 
#


#main function
def main():

    # Set For loop count start
    count = 1

    
    
    for count in range(1,6):

        #Get the test score from the user.
        test = float(input('Enter the test score:'))

        determine_grade(test)

        calc_average(test)
        
        #Print the test letter grade.
        print(determine_grade(test))

        count = count + 1

    

    #Print the average of the 5 test scores
    print('The average of the five test scores equals', calc_average(test))

        
    

# The determine_grade function returns a letter grade based on the test score.
def determine_grade(test):
    
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
       
  
    if test >= A_score:
        return 'Your grade is: A'
    elif test >= B_score and test < A_score:
        return 'Your grade is: B'
    elif test >= C_score and test < B_score:
        return 'Your grade is: C'
    elif test >= D_score and test < C_score:
        return 'Your grade is: D'
    else:
         return 'Your grade is: F'

#The calc_average function accepts 5 test scores as arguments and returns the average of the scores.
def calc_average(test):

    # initialize accumulator
    total = 0
   
    totalAvg = total + test
    return (totalAvg)/5

        
         
    
#Call the main function.
main()
