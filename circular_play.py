import turtle

def draw_circle():
    pete = turtle.Turtle()
    pete.shape("turtle")
    pete.color("white")
 
    for i in range(1,37):
     pete.circle(100)
     pete.left(10)

window = turtle.Screen()
window.bgcolor("black")
draw_circle()
window.exitonclick()
    
