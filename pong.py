import turtle

# creating a window
game_window = turtle.Screen()
game_window.title("Pong by Jonas")
game_window.bgcolor("black")

# for width and size of screen
game_window.setup(width=800, height=600)

# stops window from updating so game can move faster
game_window.tracer(0)

# Paddle and ball section
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
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)


# game section using a while loop to keep game running until conditions are met
while True:
    # ever time the loop runs, the screen will update
    game_window.update()
