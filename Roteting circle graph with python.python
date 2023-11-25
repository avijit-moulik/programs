from turtle import *
import colorsys
bgcolor('gray')
tracer (500)

def draw():
    h =0 
    for i in range (100):
        c= colorsys.hsv_to_rgb(h,1,1)
        h+=0.5
        up()
        goto(0,0)
        down()
        color('orange')
        fillcolor (c)
        begin_fill()
        rt (100)
        circle(i,15)
        fd (77)
        fd(i)
        lt(25)
        for j in range(129):
            fd(i)
            circle(j,299,steps =7)
        end_fill()
        
draw()
