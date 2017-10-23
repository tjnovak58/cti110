# CTI-110
# M5HW3 - Factorial
# Timothy Novak
# 10/22/17

# Accumulator
factorial = 1

# Prompt the user.
print('Enter a nonnegative integer?')
    
# Input the number.
number = int(input())


# Calculate the factorial for the entered number.
for number in range(1, number + 1):

    factorial = factorial*number

   
# Print the factorial.
print('The factorial of ', number, 'is:', factorial)
    
