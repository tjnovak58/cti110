# CTI-110
# M5HW2 - Running Total
# Timothy Novak
# 10/22/17

# Accumulator
runningTotal = 0

number = 0


# Calculate running total while input greater than zero .
while number >= 0:

    # Prompt the user.
    print('Enter a number?')
    
    # Input the number.
    number = int(input())

    if number >= 0:

        # Calculate running total.
        runningTotal = runningTotal + number
    

# Print the Running Total.
print('Total:', runningTotal)
    
