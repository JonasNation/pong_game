import turtle

# creating a window
game_window = turtle.Screen()
game_window.title("Pong by Jonas")
game_window.bgcolor("black")

# for width and size of screen
game_window.setup(width=800, height=600)

# stops window from updating so game can move faster
game_window.tracer(0)

# Paddle and ball section ****************************************************************
# paddle 1
paddle_one = turtle.Turtle()
paddle_one.speed(0)  # sets speed of paddle to max amount of available
paddle_one.shape("square")  # gives paddle its shape
paddle_one.color("white")
# streches width of the paddle
paddle_one.shapesize(stretch_wid=5, stretch_len=1)
paddle_one.penup()  # stops paddle from drawing lines
paddle_one.goto(-350, 0)  # set position of paddle

# paddle 2
paddle_two = turtle.Turtle()
paddle_two.speed(0)
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
