from turtle import *

from turtle_practice import square_spiral

shape("turtle")
#def square(length=100):
#    for i in range(6):
#        forward(length)
#        right(60)


#def circle_square(length=100):
#    for i in range(6):
#        forward(length)
#        right(100)


#def spiral(start_length=100):
#    for i in range(60):
#        forward(start_length+(5*i))
#        right(5)

#square()
#circle_square()
#spiral()

#from turtle import *

from turtle_practice import square_spiral

#shape("turtle")
def square1(length=100):
    for i in range(6):
        forward(length)
        left(60)


def circle_square1(length=100):
    for i in range(6):
        forward(length)
        left(100)


def spiral1(start_length=100):
    for i in range(60):
        forward(start_length+(5*i))
        left(5)

#square1()
spiral1()
#circle_square1()
#Screen().exitonclick()
input("\n\nPress Enter to exit")




