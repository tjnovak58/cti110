# CTI-110
# M2HW2 - Tip Tax Total
# Timothy Novak
# 09/10/17
#
# Get the food cost.
foodCost = float(input('Enter cost of the food: '))

# Calculate the sales tax as 7 percent of the food cost.
salesTax = foodCost * 0.07

# Calculate the tip amount as 18 percent of the food cost.
tipAmount = foodCost * 0.18

# Calculate the total cost of the meal.
totalCost = foodCost + salesTax + tipAmount

# Display the sales tax.
print('The sales tax is $', format(salesTax, ',.2f'))

# Display the tip amount.
print('The tip amount is $', format(tipAmount, ',.2f'))

# Display the total cost.
print('The total cost is $', format(totalCost, ',.2f'))
