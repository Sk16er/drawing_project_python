import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Graphics - Heart Shape")
screen.bgcolor("white")

# Create a turtle named "t"
t = turtle.Turtle()
t.speed(3)  # Set the speed of the turtle

# Set the color
t.color("red")

# Start filling the shape
t.begin_fill()

# Draw the heart shape
t.left(140)  # Turn the turtle left by 140 degrees
t.forward(180)  # Move the turtle forward by 180 units

# Draw the left curve of the heart
t.circle(-90, 200)

# Draw the right curve of the heart
t.left(120)
t.circle(-90, 200)

# Complete the heart shape
t.forward(180)

# End filling the shape
t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open until clicked
screen.mainloop()
