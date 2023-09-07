from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


is_game_on = True

def game_over():
    global is_game_on
    is_game_on = False
    scoreboard.game_over()

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # collision with food
    if snake.head.distance(food) < 17:
        food.new_location()
        scoreboard.add_point()
        snake.extend_snake()

    # check collision with food
    if snake.head.xcor() > 280 or snake.head.xcor() < - 280 \
            or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        game_over()

    # check collision with self
    if snake.check_collision():
        game_over()


screen.exitonclick()
