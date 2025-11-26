# turtle-square-and-rectangle.py
# Ben Underwood

import turtle

turtle.shape("turtle")  # optional 
# turtle.speed(0)         # optional 

def turtle_draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length) 
        turtle.left(90)

def turtle_draw_rectangle(width, height):
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

turtle.color("blue")
turtle.pensize(5)

turtle_draw_square(90)

turtle.penup()

turtle.right(180)
turtle.forward(200)
turtle.left(180)

turtle.pendown()

turtle_draw_square(90)

turtle.penup()

turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.pendown()
turtle_draw_rectangle(120, 80)


turtle.Screen().exitonclick() 