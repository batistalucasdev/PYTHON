from turtle import *

lados = 4
angulo = 360 / lados

left(angulo)

speed(11)
shape("turtle")
pensize(6)
color("Red")

for count in range(36):
    forward(100)
    right(angulo)

done()
