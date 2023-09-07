from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP_HEADING = 90
DOWN_HEADING = 270
LEFT_HEADING = 180
RIGHT_HEADING = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, pos):
        segment = Turtle(shape='square')
        segment.color('white')
        segment.penup()
        segment.goto(pos)
        self.snake_body.append(segment)

    def extend_snake(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if not self.head.heading() == DOWN_HEADING:
            self.head.setheading(UP_HEADING)

    def down(self):
        if not self.head.heading() == UP_HEADING:
            self.head.setheading(DOWN_HEADING)

    def left(self):
        if not self.head.heading() == RIGHT_HEADING:
            self.head.setheading(LEFT_HEADING)

    def right(self):
        if not self.head.heading() == LEFT_HEADING:
            self.head.setheading(RIGHT_HEADING)

    def check_collision(self):
        for segment in self.snake_body[1:]:
            return self.head.distance(segment) < 10

