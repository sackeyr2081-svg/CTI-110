# Raphael Sackey
# 11/28/2025
# P4LAB1 - Turtle House
# Draws a house (square + triangle) using both a for loop and a while loop.

import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("P4LAB1 House Drawing")
screen.bgcolor("lightblue")   # background color

# Create the turtle
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("darkgreen")        # line color
pen.pensize(3)
pen.speed(3)

# Move turtle to starting position for the house body
pen.penup()
pen.goto(-50, -100)           # bottom-left corner of the square
pen.pendown()

# Draw the square (house body) using a FOR loop
side_length = 100

for _ in range(4):
    pen.forward(side_length)
    pen.left(90)

# Move to the top-left corner of the square to start the roof
pen.penup()
pen.goto(-50, 0)              # top-left corner of square
pen.setheading(0)             # face to the right
pen.pendown()

# Change color for the roof
pen.color("green")

# Draw the roof (triangle) using a WHILE loop
sides_drawn = 0
while sides_drawn < 3:
    pen.forward(side_length)
    pen.left(120)
    sides_drawn += 1

# Keep the window open
turtle.done()
