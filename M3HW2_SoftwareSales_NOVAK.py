# CTI-110
# M3HW2 - Software Sales 
# Timothy Novak
# 09/24/17
#
# This program takes as input the number of software packages purchased.
# It then displays the discount, if any, based on the quantity purchased and
# the total purchase cost with the discount applied.
#

quantity = float(input('Enter total number of software packages purchased: '))

def main():

  
    if quantity < 10:
        print('There is no discount for ', quantity, ' software package(s) purchased')
        Total = quantity * 99
        print('Total purchase cost equals $', format(Total, ',.2f'))
    if quantity >= 10 and quantity < 20:
        print('Your discount is 10 percent')
        Discount = 99 * 0.1
        Total = quantity * (99 - Discount)
        print('Total purchase cost equals $', format(Total, ',.2f'))
    if quantity >= 20 and quantity < 50:
        print('Your discount is 20 percent')
        Discount = 99 * 0.2
        Total = quantity * (99 - Discount)
        print('Total purchase cost equals $', format(Total, ',.2f'))
    if quantity >= 50 and quantity < 100:
        print('Your discount is 30 percent')
        Discount = 99 * 0.3
        Total = quantity * (99 - Discount)
        print('Total purchase cost equals $', format(Total, ',.2f'))
    if quantity >= 100:
        print('Your discount is 40 percent')
        Discount = 99 * 0.4
        Total = quantity * (99 - Discount)
        print('Total purchase cost equals $', format(Total, ',.2f'))
    
main()

