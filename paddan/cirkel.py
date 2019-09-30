import turtle

emil = turtle.Turtle()

colors = ["DarkSeaGreen", "coral", "DarkOrchid4", "hotpink", "cyan3", "lavender", "DarkBlue", "OldLace", "PeachPuff"]

for color in colors:
    emil.color(color)
    emil.begin_fill()
    emil.circle(100)
    emil.end_fill()
    emil.forward(10)
