# CTI-110
# M3TLAB - Debugging
# Timothy Novak
# 09/24/17
#
# This program takes a number grade and outputs a letter grade.
# System uses 10-point grading scale
#

score = float(input('Enter score: '))

def main():

   

    

    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
       
  
    if score >= A_score:
        print('Your grade is: A')
    elif score >= B_score and score < A_score:
        print('Your grade is: B')
    elif score >= C_score and score < B_score:
        print('Your grade is: C')
    elif score >= D_score and score < C_score:
        print('Your grade is: D')

    else:
         print('Your grade is: F') 
main()

