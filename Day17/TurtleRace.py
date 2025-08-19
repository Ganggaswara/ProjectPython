from turtle import Turtle, Screen
import random
import tkinter as tk
from tkinter import messagebox, simpledialog

colors = ["red", "blue", "green", "purple",
          "black", "orange", "pink", "brown", "gray"]

def pick_colors():
    return random.sample(colors, 5)

unique_colors = pick_colors()
distance_forward = [10, 5, 15]

tim = Turtle()
tim.hideturtle()
tim.penup()
tim.goto(400, 250)
tim.pensize(4)
tim.pendown()
tim.goto(400, -20)
tim.penup()
tim.goto(370, 270)
tim.write("FINISH", font=("Montserrat", 15, "bold"))

base_turtle = Turtle()
base_turtle.shape("turtle")
base_turtle.color("black")

turtles = []
finish = False
for i in range(5):
    turtle = base_turtle.clone()
    turtle.color(unique_colors[i])
    turtle.penup()
    turtle.goto(-400, (i * 50))  # Posisi berurutan: 40, 60, 80, 100, 120
    turtles.append(turtle)

base_turtle.hideturtle()
bet = tk.simpledialog.askstring(
    "Turtle Race!", "Which color turtle do u bet? ")

while bet is None:
    messagebox.showinfo(
        "Turtle Race", f"You did'nt choose one of the turtles! ")
    bet = tk.simpledialog.askstring(
        "Turtle Race!", "Which color turtle do u bet? ")

while bet.lower() not in [color.lower() for color in unique_colors]:
    messagebox.showinfo("Turtle Race", f"Wrong color the turtles! ")
    bet = tk.simpledialog.askstring(
        "Turtle Race!", "Which color turtle do u bet? ")

while not finish:
    for t in turtles:
        t.forward(random.choice(distance_forward))
        if t.xcor() >= 400:
            winning_color = t.color()[0]
            finish = True

if bet.lower() == winning_color.lower():
    messagebox.showinfo("Turtle Race", f"You Win, {winning_color} turtle win!")
else:
    messagebox.showinfo(
        "Turtle Race", f"You Lose, the winner is {winning_color} turtle")
screen = Screen()
screen.exitonclick()
