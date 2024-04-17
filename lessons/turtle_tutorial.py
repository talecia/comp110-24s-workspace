"""Turtle Tutorial."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.penup()
leo.goto(45, 60)
leo.pendown()


i: int = 0 
while (i < 3): 
    leo.forward(300)
    leo.left(120)
    i = i + 1


colormode(255)
leo.color(99)
leo.begin_fill()
 # code for shape to be filled 
leo.end_fill()

leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.color("green", "yellow")