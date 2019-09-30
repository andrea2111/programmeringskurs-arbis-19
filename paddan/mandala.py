import turtle
import random

emil = turtle.Turtle()

emil.speed("fast")


colors = ["DarkSeaGreen", "coral", "DarkOrchid4", "hotpink", "cyan3", "lavender",
          "DarkBlue", "OldLace", "PeachPuff"]

for i in range(8):
    for i in range(8):
        emil.color(random.choice(colors))
        emil.circle(100)
        emil.left(45)
    emil.left(20)



