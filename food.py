from random import randint
from turtle import Turtle


X = randint(-280, 280)  # generating a random coordinate for X axis
Y = randint(-280, 280)  # generating a random coordinate for Y axis



class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.goto(X, Y)
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        print(f"Coordinate value of the food ({X}, {Y})\n")
