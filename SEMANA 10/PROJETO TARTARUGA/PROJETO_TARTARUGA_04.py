from turtle import *

speed(11)
shape("turtle")

color("Red")
for count in range(5):
    forward(100)
    right(72)

penup()
left(90)
forward(150)
pendown()
color("Blue")

for count in range(6):
    forward(100)
    right(60)

penup()
left(90)
forward(100)
pendown()
color("Gray")

for count in range(360):
    forward(1)
    left(1)


done()
