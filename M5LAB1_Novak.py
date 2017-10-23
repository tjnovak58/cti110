# CTI-110
# M5LAB1 - Shapes
# Timothy Novak
# 10/22/17

# Call turtle module.
import turtle

wn = turtle.Screen()
tim = turtle.Turtle()

# Draw a square.
for count in range(4):
    
    tim.right(90) 
    tim.forward(100)
    

# Draw a triangle.
for count in range(2):

    tim.right(-120)
    tim.forward(100)
    
wn.exitonclick()
