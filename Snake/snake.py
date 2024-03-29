from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake_seg = []
        self.create_snake()
        self.head = self.snake_seg[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.snake_seg.append(new_segment)

    def reset(self):
        for seg in self.snake_seg:
            seg.goto(1000, 1000)
        self.snake_seg.clear()
        self.create_snake()
        self.head = self.snake_seg[0]

    def extend(self):
        self.add_segment(self.snake_seg[-1].position())

    def move(self):
        for seg in range(len(self.snake_seg) - 1, 0, -1):
            new_x = self.snake_seg[seg - 1].xcor()
            new_y = self.snake_seg[seg - 1].ycor()
            self.snake_seg[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
