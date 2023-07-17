from turtle import Turtle
import random

colors = ['red', "blue", "pink", "yellow", "gray", "purple", "green"]



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")


    def refresh(self):
        x_cor = random.randint(-380, 380)
        y_cor = random.randint(-380, 380)
        self.goto(x_cor, y_cor)
        self.color(random.choice(colors))




