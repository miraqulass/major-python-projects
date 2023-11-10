# import required modules
import turtle
import time
import random

delay = 0.15
score = 0
high_score = 0

# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
# the width and height can be put as user's choice
wn.setup(width=600, height=600)
wn.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Right"

# snake body
segments = []

# food in the game
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# score display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score : 0 High Score : 0", align="center", font=("Courier", 24, "normal"))


# assigning key directions
def go_up():
    if head.direction != "Down":
        head.direction = "Up"


def go_down():
    if head.direction != "Up":
        head.direction = "Down"


def go_left():
    if head.direction != "Right":
        head.direction = "Left"


def go_right():
    if head.direction != "Left":
        head.direction = "Right"


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main Gameplay
while True:
    wn.update()

    if head.direction == 'Up':
        head.sety(head.ycor() + 20)
    elif head.direction == 'Down':
        head.sety(head.ycor() - 20)
    elif head.direction == 'Left':
        head.setx(head.xcor() - 20)
    elif head.direction == 'Right':
        head.setx(head.xcor() + 20)

    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Right"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.15
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("green")   # tail colour
        new_segment.penup()
        segments.append(new_segment)
        # delay -= 0.001
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("Courier", 24, "normal"))

# Checking for head collisions with body segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    for segment in segments:
        if head.distance(segment) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Right"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = 0.15
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

# wn.mainloop()