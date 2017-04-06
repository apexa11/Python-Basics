# turtle use for draw any kind of shapes

import turtle


def loop_square(some_turtle):
    i = 1
    while i <= 4:
        some_turtle.forward(100)
        some_turtle.right(90)
        i = i + 1


def draw_square():

    # one way to start draw

    brad = turtle.Turtle()

    # customised turtle

    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(3)
    for i in range(1, 37):
        loop_square(brad)
        brad.right(10)
    for i in range(38, 39):
        brad.right(90)
        brad.forward(300)



			
