import turtle

def draw_squares():
    t = turtle.Turtle()
    t.speed(0)

    for i in range(60):
            for j in range(4):
                t.forward(100)
                t.right(90)
            t.right(5)
draw_squares()
turtle.done()