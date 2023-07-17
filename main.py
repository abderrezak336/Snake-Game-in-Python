from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
import pygame



pygame.mixer.init()
pygame.mixer.music.load(r"sound.mp3")
tim = Turtle()




screen = Screen()
screen.title("SNAKE GAME")
screen.bgcolor("black")
screen.setup(width=800, height=800)

screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

snake.creat_snake()


screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.left, "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detect collision with head and food
    if snake.head.distance(food) < 20:
        pygame.mixer.music.play()
        score_board.increase_score()
        food.refresh()
        snake.extend()

    #detect collision with head and wall
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        snake.remove()
        score_board.reset()


    #detect collision with head and body
    for seg in snake.segments[1::]:
        if snake.head.distance(seg) < 10:
            snake.remove()
            score_board.reset()



















screen.exitonclick()