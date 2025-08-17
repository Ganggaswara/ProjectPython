from turtle import Turtle, Screen
import random
import colorgram
import turtle

niko = Turtle()
niko.hideturtle()
niko.shape("turtle")
niko.speed("fastest")
turtle.colormode(255)
colors = colorgram.extract('Day16/bank_color.jpg', 20)
niko.penup()
niko.goto(-400,-350)
y_pos = niko.ycor()
for _ in range(50):
    for i in range(21):
        bank_colors = random.choice(colors)
        rgb = tuple(bank_colors.rgb)
        niko.dot(15, rgb)
        niko.penup()
        niko.forward(40)

    y_pos += 40
    niko.penup()
    niko.goto(-400, y_pos)


screen = Screen()
screen.exitonclick()
