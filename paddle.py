from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, starting_x):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(starting_x, 0)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
