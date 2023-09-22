from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()

snake = Snake()
food = Food()

snake_speed = screen.textinput("Speed",
                               "Please choose a speed (N for normal, F for fast, S for slow) : ")

sleep_time = 0.1

# print(snake_speed)

if snake_speed is not None:
    snake_speed = snake_speed.lower()
    # print(snake_speed)
    if snake_speed == "n":
        sleep_time = 0.5
        # print("n")
    elif snake_speed == "f":
        sleep_time = 0.1
        # print("f")

    elif snake_speed == "s":
        sleep_time = 1
        # print("s")

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(sleep_time)
    snake.move_snake()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.increase_snake_size()
        scoreboard.refresh_score()

    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    for i in range(1, len(snake.all_turtles)):
        if snake.head.distance(snake.all_turtles[i]) < 15:
            game_is_on = False
            scoreboard.game_over()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

screen.exitonclick()
