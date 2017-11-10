# This program uses a value-returning function to convert feet to inches and
# print the answer.
# 11/10/17
# CTI-110 M6T2_FeetToInches
# Timothy Novak
# 
#

# Constant for the number of inches per foot.
INCHES_PER_FOOT = 12

#main function
def main():
    #Get number of feet from the user.
    feet = int(input('Enter the number of feet:'))

    #Convert input to inches.
    print(feet, 'feet equals', feet_to_inches(feet), 'inches.')
    
#The feet_to_inches function converts feet to inches.
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT
    
#Call the main function.
main()
