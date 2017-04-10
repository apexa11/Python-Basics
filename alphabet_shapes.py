import turtle
def draw_Aalphabet():
    apexa = turtle.Turtle()
    apexa.shape("turtle")
    apexa.color("blue")
    apexa.left(120)
    apexa.forward(200)
    apexa.right(-120)
    apexa.forward(200)
    apexa.backward(100)
    apexa.right(-120)
    apexa.forward(100)
    apexa.setpos(0,0)

#for K
    apexa.right(-90)
    apexa.forward(170)
    apexa.backward(80)
    apexa.right(65)
    apexa.forward(120)
    apexa.backward(120)
    apexa.left(-65)
    apexa.forward(120)
 
    
 


window=turtle.Screen()
window.bgcolor("pink")
draw_Aalphabet()


window.exitonclick()

