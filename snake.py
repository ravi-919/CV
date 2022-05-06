from turtle import Turtle, Screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_objects = []
        self.create_snake()
        self.head = self.snake_objects[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake = Turtle('square')
        new_snake.color('white')
        new_snake.penup()
        new_snake.goto(position)
        self.snake_objects.append(new_snake)

    def reset(self):
        for seg in self.snake_objects:
            seg.goto(1000, 1000)
        self.snake_objects.clear()
        self.create_snake()
        self.head = self.snake_objects[0]


    def extend(self):
        self.add_segment(self.snake_objects[-1].position())

    def move(self):
        for i in range(len(self.snake_objects) - 1, 0, -1):
            x_cor = self.snake_objects[i - 1].xcor()
            y_cor = self.snake_objects[i - 1].ycor()
            self.snake_objects[i].goto(x_cor, y_cor)
        self.snake_objects[0].forward(20)

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