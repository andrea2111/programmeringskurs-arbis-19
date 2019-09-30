import turtle
import random

emil = turtle.Turtle()


for i in range(10):
    x = random.randrange(-200, 200)
    y = random.randrange(-200, 200)
    emil.penup()
    emil.goto(x, y)
    emil.pendown()
    for i in range(5):
        emil.forward(50)
        emil.right(144)