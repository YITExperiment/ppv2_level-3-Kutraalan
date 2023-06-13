import turtle

from itertools import cycle
colors=cycle(['red','orange','yellow','green','blue','puple'])

def draw_shape(size,angle,shift,shape):
    turtle.pencolor(next(colors))
    next_shape =''
    if shape == 'circle':
        turtile.circle(size)
        next_shape = 'square'
    elifshape == 'square'
        for 1 in range(4):
            turtle.forward(size + 2)
            tutle.left(90)
       next_shape = 'circle'
    turtle.right(angle)
    turtle.forward(shift)
    draw_shape(size+5,angle+1,shift+1,next_shape)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(30,0,1,'circle')
