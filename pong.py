import turtle

# creating a window
game_window = turtle.Screen()
game_window.title("Pong by Jonas")
game_window.bgcolor("black")

# for width and size of screen
game_window.setup(width=800, height=600)

# stops window from updating so game can move faster
game_window.tracer(0)

# Score
player_one_score = 0
player_two_score = 0

# Paddle and ball section ****************************************************************
# paddle 1
paddle_one = turtle.Turtle()
paddle_one.speed("fastest")  # sets speed of paddle to max amount of available
paddle_one.shape("square")  # gives paddle its shape
paddle_one.color("white")
# streches width of the paddle
paddle_one.shapesize(stretch_wid=5, stretch_len=1)
paddle_one.penup()  # stops paddle from drawing lines
paddle_one.goto(-350, 0)  # set position of paddle

# paddle 2
paddle_two = turtle.Turtle()
paddle_two.speed("fastest")
paddle_two.shape("square")
paddle_two.color("white")
paddle_two.shapesize(stretch_wid=5, stretch_len=1)
paddle_two.penup()
paddle_two.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# ball movement on y and x axis 2 pixels
ball.dx = 0.1
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center",
          font=("Courier", 24, "normal"))


# functions will have code for moving paddles up and down **********************************


def paddle_one_up():
    # returns the y coordinants for paddle one
    y = paddle_one.ycor()
    # for paddle to move up and down, add and subtract
    y += 20
    paddle_one.sety(y)


def paddle_one_down():
    y = paddle_one.ycor()
    y -= 20
    paddle_one.sety(y)


def paddle_two_up():
    # returns the y coordinants for paddle one
    y = paddle_two.ycor()
    # for paddle to move up and down, add and subtract
    y += 20
    paddle_two.sety(y)


def paddle_two_down():
    y = paddle_two.ycor()
    y -= 20
    paddle_two.sety(y)


# keyboard binding

# listens for keyboard input
game_window.listen()
# when the a key is pressed func paddle one up is called to move paddle
game_window.onkeypress(paddle_one_up, "w")
game_window.onkeypress(paddle_one_down, "s")
game_window.onkeypress(paddle_two_up, "Up")
game_window.onkeypress(paddle_two_down, "Down")


# game section using a while loop to keep game running until conditions are met **************
while True:
    # ever time the loop runs, the screen will update
    game_window.update()

    # makes ball move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check - once ball get to a certain point it will bounce off, by compairing the ball y coordinates
    # top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # reverses the direction of ball
    # bottom border
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    # right border
    elif ball.xcor() > 390:
        # ball.goto(0, 0)
        ball.setx(390)
        ball.dx *= -1
        player_one_score += 1
        pen.clear()
        pen.write("Player 1: {0}  Player 2: {1}".format(player_one_score, player_two_score), align="center",
                  font=("Courier", 24, "normal"))
    # left border
    elif ball.xcor() < -390:
        # ball.goto(0, 0)
        ball.setx(-390)
        ball.dx *= -1
        player_two_score += 1
        pen.clear()
        pen.write("Player 1: {0}  Player 2: {1}".format(player_one_score, player_two_score), align="center",
                  font=("Courier", 24, "normal"))

    # get ball to bounce off paddle
    # paddle two
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_two.ycor() + 55 and ball.ycor() > paddle_two.ycor() - 55):
        ball.setx(340)
        ball.dx *= -1
    # paddle one
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_one.ycor() + 55 and ball.ycor() > paddle_one.ycor() - 55):
        ball.setx(-340)
        ball.dx *= -1
