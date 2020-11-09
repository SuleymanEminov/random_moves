from turtle import Turtle, Screen
import random

tim = Turtle()

tim.color("Blue")
tim.pensize(15)
tim.speed(10)

moves = [90, 0, 180,270]

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)

def move():
    for i in range(300):
        change_color()

        tim.setheading(random.choice(moves))


        tim.forward(30)


move()



screen = Screen()
screen.exitonclick()

