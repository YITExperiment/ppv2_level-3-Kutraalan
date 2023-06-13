import turtle

from itertools import cycle
colors=cycle(['red','orange','yellow','green','blue','puple'])

def draw_circle(size,angle,shift):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+20,angle+25,shift+10)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(30,0,1)
