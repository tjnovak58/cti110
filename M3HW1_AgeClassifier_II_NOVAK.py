# CTI-110
# M3HW1 - Age Classifier
# Timothy Novak
# 09/24/17
#
# This program takes an age input and outputs a classification.
#

age = float(input('Enter age: '))

def main():

  
    if age >= 20:
        print('The person is an Adult')
    elif age >= 13:
        print('The person is a Teenager')
    else:
      
        if age > 1:
            print('The person is a Child')
        else: 
            print('The person is an Infant')
    
main()

