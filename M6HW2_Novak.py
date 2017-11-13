# Number guessing game.  Program uses import and employs random number generator.
# Asks user to guess number and tells them if their guess is too high or
# too low. If number is not guessed, it asks the user to try again.
# 11/13/17
# CTI-110 M6HW2 - Random Number Guessing Game
# Timothy Novak
# 

# use the random module
import random

# set constant values for minimum, maximum (game uses from 1 to 100)
MIN = 1
MAX = 100

def main():
    # use a variable to control the loop
    again = 'y'
 
    
    # until the user is finished, repeat
    while again == 'y' or again == 'Y':

        play_game()

        print('Congratulations! You guessed the number!')

                
        # play again?
        again= input('Play again? (y = yes): ')

def play_game():

        # simulate generating random number
        print('Generating random number between 1 and 100...')

        number = random.randint(MIN, MAX)

        guess = ()
                
        while guess != number:

                        
            guess = int(input('What is your guess?'))

            if guess > number:

                print('Your guess is too high. Guess lower.')
                               

            elif guess < number:

                print('Your guess is too low. Guess higher')

  
                                    

# call the main() function
main()
