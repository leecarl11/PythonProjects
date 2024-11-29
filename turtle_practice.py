#from operator import length_hint
from turtle import *
from turtledemo.penrose import start
speed(0)
shape("turtle")

def square(forward_distance=100, right_angle=90):
    for i in range(4):
        forward(forward_distance)
        right(right_angle)

def circle_squares(length=100):
    for i in range(60):
        square(length)
        right(5)

def triangle(length=100):
    for i in range(3):
        forward(length)
        right(120)

def star(length=100):
    for i in range(5):
        forward(length)
        right(144)

def square_spiral(start_length=5):
    for i in range(60):
        square(start_length+(5*i))
        right(5)

#triangle()
#square()
square_spiral()
#Screen() .exitonclick()
input("\n\nPress the enter key to exit.")