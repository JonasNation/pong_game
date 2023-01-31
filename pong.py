import turtle

# creating a window
game_window = turtle.Screen()
game_window.title("Pong by Jonas")
game_window.bgcolor("black")

# for width and size of screen
game_window.setup(width=800, height=600)

# stops window from updating so game can move faster
game_window.tracer(0)


# game section using a while loop to keep game running until conditions are met
while True:
    # ever time the loop runs, the screen will update
    game_window.update()
