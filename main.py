from turtle import Turtle, Screen, colormode
import random

rgb_colors = [(153, 91, 49), (209, 156, 107), (42, 111, 146), (60, 116, 75), (199, 157, 31), (240, 58, 34),
              (131, 170, 183), (248, 211, 75), (155, 7, 26), (145, 64, 87), (146, 219, 161), (29, 178, 108),
              (188, 132, 139), (253, 232, 0), (125, 181, 123), (23, 55, 82), (222, 49, 52), (193, 234, 198),
              (46, 151, 194), (17, 90, 59), (250, 147, 138), (3, 78, 45), (250, 146, 159), (218, 231, 237),
              (192, 26, 13), (245, 229, 232), (3, 82, 118), (81, 71, 41), (46, 62, 86)]

tim = Turtle()
colormode(255)
tim.penup()


def position():
    for _ in range(9):
        tim.dot(50, random.choice(rgb_colors))
        tim.forward(100)


x = -400
y = -400

for _ in range(9):
    tim.setx(x)
    tim.sety(y)
    position()
    y += 100


screen = Screen()
screen.screensize()
screen.exitonclick()
