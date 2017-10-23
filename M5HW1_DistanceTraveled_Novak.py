# CTI-110
# M5HW1 - Distance Traveled
# Timothy Novak
# 10/22/17


# Prompt the user.
print('What is the speed of the vehicle in mph?')
    
# Input the speed of the vehicle.
speed = int(input())

# Prompt the user.
print('How many hours has it traveled?')
    
#  Input the hours it has traveled.
time = int(input())



# Accumulator
count = time + 1

# Print the distance traveled by hour.
for time in range(1,count):

    # Formula to calculate distance traveled.
    distance = speed * time
    

    # Display distance traveled by hour.
    print('Hour', 'Distance Traveled')
    print('====', '=================')
    print(time, distance, sep='\t')
