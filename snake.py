MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    from turtle import Turtle

    def __init__(self):
        self.all_turtles = []
        self.create_snake_body()
        self.head = self.all_turtles[0]
        # self.num_of_segment = 3

    def create_snake_body(self):
        x_cor = 0
        for i in range(3):
            new_turtle = self.Turtle(shape='square')
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(x=x_cor, y=0)
            x_cor -= 20
            self.all_turtles.append(new_turtle)

    def increase_snake_size(self):
        tail_xcor = self.all_turtles[len(self.all_turtles) - 1].xcor()
        tail_ycor = self.all_turtles[len(self.all_turtles) - 1].ycor()

        # print(f"{tail_xcor} {tail_ycor}")
        new_turtle = self.Turtle(shape='square')
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(x=tail_xcor, y=tail_ycor)
        self.all_turtles.append(new_turtle)
        # print(self.all_turtles)

    def move_snake(self):

        for turtle_num in range(len(self.all_turtles) - 1, 0, -1):
            self.all_turtles[turtle_num].goto(self.all_turtles[turtle_num - 1].pos())

        self.all_turtles[0].forward(MOVE_DISTANCE)

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
