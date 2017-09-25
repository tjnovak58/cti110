# CTI-110
# Question M3Q2_N-Z 
# Timothy Novak
# 09/24/17
#
# This program takes as input the temperature of a sample of water in degrees celsius.
# It then displays the type of the water depending on what temperature range it falls into.
#

SampleTemp = float(input('Enter the temperature of a sample of water in degrees celsius: '))

def main():

  
    if SampleTemp <= 0:
        print('The water sample type is Ice')
        
    if SampleTemp > 0 and SampleTemp <= 100:
        print('The water sample type is Liquid Water')
        
    if SampleTemp > 100:
        print('The water sample type is Steam')
        
        
main()
