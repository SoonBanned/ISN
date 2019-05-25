from turtle import *
from math import *

def schema(ax,ay,bx,by, n):
    speed(0)
    ht()
    if n == 0:
        return
    goto(ax, ay)
    l = sqrt(((bx-ax)**2 + (by-ay)**2))
    print(l)
    T = degrees(acos(((bx-ax)/l)))
    print(T)
    ac = sqrt((l**2)/2)
    ai = l/2
    ci = sqrt(ac**2-ai**2)
    if (by-ay) > 0:
        seth(T)
    else:
        seth(-T)
    down()
    for i in range (4):
        if i == 2:
            x4 = xcor()
            y4 = ycor()
        if i == 3:
            x3 = xcor()
            y3 = ycor()
        forward(l)
        left(90)
    up()
    right(90)
    backward(l)
    left(90)
    forward(l/2)
    left(90)
    forward(ci)
    x5 = xcor()
    y5 = ycor()
    schema(x3,y3,x5,y5, n-1)
    schema(x5,y5,x4,y4, n-1)