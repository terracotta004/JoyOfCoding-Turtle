# house.py
# Ben Underwood

import turtle

def turtle_draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length) 
        turtle.left(90)

def turtle_draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

def turtle_draw_house(side_length):
    turtle_draw_square(side_length)
    turtle.left(90)
    turtle.forward(side_length)
    turtle.right(90)
    turtle_draw_triangle(side_length)
    turtle.right(90)
    turtle.forward(side_length)
    turtle.left(90)

turtle_draw_house(100)

turtle.penup()

turtle.backward(200)

turtle.pendown()

turtle_draw_house(150)

turtle.Screen().exitonclick()