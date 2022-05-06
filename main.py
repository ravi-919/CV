from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score

screen = Screen()
screen.bgcolor("black")
screen.title("The snake game")
screen.setup(width=600, height=600)
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_update()

    #Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score.reset()
        snake.reset()

    #detect collision with itself
    #If head collides with any segment in the tail then trigger the game_over sequence

    for snake_parts in snake.snake_objects[1:]:
        if snake.head.distance(snake_parts) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()