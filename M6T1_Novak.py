# CTI-110
# M6T1 - Kilometer Converter
# Timothy Novak
# 11/09/17
#
# This program prompts the user to enter a distance in kilometers.
# It then converts the distance from kilomters to miles.
#

conversion_factor = 0.6214

def main():
    kilometers = float(input('Enter the distance traveled in kilometers:'))
    show_miles(kilometers)

def show_miles(km):
    miles = km * conversion_factor
    print('Distance traveled in miles = ', miles)

    

main()
