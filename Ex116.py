import turtle
import colorsys


t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
n = 36
h = 0
for i in range(200):
    c = colorsys.hsv_to_rgb(h, 1, 0.9)
    h += 1/n
    t.color(c)
    t.left(180)
    for j in range(5):
        t.forward(75)
        t.left(356)
    if i == 199:
        p = str(input('?'))
        