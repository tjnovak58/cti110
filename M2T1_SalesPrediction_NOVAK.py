# CTI-110
# M2T1 - Sales Prediction
# Timothy Novak
# 09/10/17
#
# Get the projected total sales.
totalSales = float(input('Enter the projected total sales: '))

# Calculate the profit as 23 percent of total sales.
annualProfit = totalSales * 0.23

# Display the profit.
print('The annual profit is $', format(annualProfit, ',.2f'))
