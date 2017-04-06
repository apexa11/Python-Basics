import turtle

def draw_circle():
    pete = turtle.Turtle()
    pete.shape("turtle")
    pete.color("red")
 
    for i in range(1,37):
     pete.circle(100)
     pete.left(10)

window = turtle.Screen()
window.bgcolor("yellow")
draw_circle()
window.exitonclick()
    
