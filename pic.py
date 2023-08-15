import turtle
import colorsys

# Set up the turtle screen
turtle.bgcolor("white")
turtle.speed(0)  # Fastest drawing speed

# Set the initial position
turtle.penup()
turtle.goto(-400, -100)
turtle.pendown()

# Define rainbow colors using HSV color space
colors = [(0.99, 0.13, 1),    # Red
          (0.98, 0.48, 1),    # Orange
          (0.95, 0.80, 1),    # Yellow
          (0.50, 1.00, 1),    # Green
          (0.15, 1.00, 1),    # Blue
          (0.72, 0.60, 1)]    # Purple

# Draw the rainbow
turtle.width(20)
for color in colors:
    turtle.pencolor(color)
    turtle.circle(400, 60)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.circle(400, 60)
    turtle.penup()
    turtle.goto(-400, -100)
    turtle.pendown()

# Hide the turtle and display the result
turtle.hideturtle()
turtle.done()
