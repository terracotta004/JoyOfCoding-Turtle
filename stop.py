# stop.py
# Ben Underwood

import turtle

turtle.speed(1)

def turtle_draw_rectangle(width, height):
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

def turtle_draw_octagon(side_length):
    for _ in range(8):
        turtle.forward(side_length)
        turtle.left(45)

def turtle_draw_stop_sign(side_length):
    turtle.color("red")
    turtle_draw_octagon(side_length)
    turtle.penup()
    turtle.forward(side_length * 3 / 8)
    turtle.right(90)
    turtle.forward(side_length * 2)
    turtle.left(90)
    turtle.pendown()
    turtle_draw_rectangle(side_length * 1 / 5, side_length * 2)
    turtle.penup()
    turtle.left(90)
    turtle.forward(side_length * 2)
    turtle.right(90)
    turtle.pendown()

turtle_draw_stop_sign(100)

turtle.penup()

turtle.left(180)

turtle.forward(250)

turtle.right(180)

turtle.pendown()

turtle_draw_stop_sign(20)

turtle.Screen().exitonclick()