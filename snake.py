from turtle import Turtle




POSITION = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.creat_snake()
        self.head = self.segments[0]




    def creat_snake(self):
        for pos in POSITION:
            self.add_new_segment(pos)
    def remove(self):
        for seg in self.segments:
            seg.goto(1000, 1000)

        self.segments.clear()
        self.creat_snake()
        self.head = self.segments[0]



    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(20)

    def add_new_segment(self, position):
        tim = Turtle()
        tim.penup()
        tim.shape("square")
        tim.color("white")
        tim.goto(position)
        self.segments.append(tim)

    def extend(self):
        self.add_new_segment(self.segments[-1].position())


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

