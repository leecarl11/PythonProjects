from turtle import *
shape("turtle")
speed(0)
def square(num_squares,angle_turn):
    for i in range(num_squares):
     for i in range(4):
        forward(100)
        right(90)
        right(angle_turn)
square(60,5)
