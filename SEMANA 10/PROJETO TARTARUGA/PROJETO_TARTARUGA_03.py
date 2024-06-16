from turtle import *

speed(11)
shape("turtle")

for count in range(8):
    forward(100)
    right(45)

left(90)
penup()
forward(20)

for count in range(30):
    forward(5)
    penup()
    forward(5)
    pendown()
    
done()
