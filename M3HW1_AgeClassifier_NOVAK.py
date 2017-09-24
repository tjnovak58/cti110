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
    if age >= 13 and age < 20:
        print('The person is a Teenager')
    if age > 1 and age < 13:
        print('The person is a Child')
    if age <= 1:
        print('The person is an Infant')
    
main()

