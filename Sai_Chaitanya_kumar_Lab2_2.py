import turtle
from turtle import *
def test_drive():
    turtle.pensize(5)
    turtle.forward(100)
    turtle.left(87)
    turtle.setheading(127)
    turtle.down()
    turtle.goto(50,50)
    turtle.home()
    turtle.circle(25)
def turtle_state():
    print(turtle.isdown())
    print(turtle.heading())
    print(turtle.xcor())
    print(turtle.ycor())
    
turtle_state()
test_drive()
turtle_state()
