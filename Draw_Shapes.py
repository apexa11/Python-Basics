#turtle use for draw any kind of shapes
import turtle

def draw_square():
    #one way to start draw
    brad = turtle.Turtle()
    #customised turtle
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(3)

    #make square here
    i=1
    while(i <= 4):
     brad.forward(100)
     brad.right(90)
     i=i+1

    #make circle using turtle
def draw_circle():
    pete = turtle.Turtle()
    pete.shape("turtle")
    pete.color("blue")
    pete.circle(100)
    pete.speed(2)

 #make triangle
def draw_triangle():
    angie=turtle.Turtle()
    angie.shape("turtle")
    angie.color("black")
    angie.speed(2)

    j=1
    while(j <= 3):
     angie.forward(100)
     angie.left(120)
     j=j+1

#for red carpet background need window screen red
window = turtle.Screen()
window.bgcolor("red")
draw_square()
draw_circle()
draw_triangle()
window.exitonclick()
    


