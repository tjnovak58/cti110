# CTI-110
# M5LAB2 - Initials
# Timothy Novak
# 10/22/17

# Call turtle drawing.
import turtle

wn = turtle.Screen()
tim = turtle.Turtle()

# Set Pen Color.
tim.color("purple")

# Set Pen Size.
tim.pensize(5)

# Draw initials.
tim.forward(50)
tim.right(90)
tim.forward(100)
tim.forward(-100)
tim.right(-90)
tim.forward(50)
tim.penup()
tim.forward(50)
tim.pendown()
tim.right(90)
tim.forward(100)
tim.forward(-100)
tim.left(30)
tim.forward(115)
tim.left(150)
tim.forward(105)

wn.exitonclick()

    
