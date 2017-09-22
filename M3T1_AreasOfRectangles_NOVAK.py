# CTI-110
# M3T1 - Areas of Rectangles
# Timothy Novak
# 09/22/17
#
# Get the dimensions of rectangle 1.
L1 = int(input('Enter the length of rectangle 1: '))
W1 = int(input('Enter the width of rectangle 1: '))

# Get the dimensions of rectangle 2.
L2 = int(input('Enter the length of rectangle 2: '))
W2 = int(input('Enter the width of rectangle 2: '))

# Calculate the areas of the rectangles.
RA1 = L1 * W1
RA2 = L2 * W2

#Determine which rectangle has the larger area.
if RA1 > RA2:
    print('Rectangle 1 has the larger area.')
elif RA2 > RA1:
    print('Rectangle 2 has the larger area.')
else:
    print('Both rectangles have the same area.')


