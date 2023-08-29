from turtle import Turtle


class State(Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.state = state
        self.x = x
        self.y = y
        self.penup()
        self.color('black')
        self.goto(x=self.x, y=self.y)
        self.write(arg=self.state)
        self.hideturtle()
