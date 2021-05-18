from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # creating a constant position of the snake
MOVE_DISTANCE = 20  # creating a constant moving distance of the snake
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    This is the snake itself.
    Beware it might bite you :D
    """

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            t.goto(position)
            self.segments.append(t)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            print(f"X_coordinate: {new_x}, Y_coordinate: {new_y}")
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
