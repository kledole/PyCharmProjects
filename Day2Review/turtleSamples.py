# File: turtle.py
# Description: resuming review of python programming
# The following exercises demonstrate the use of turtle drawing library.
# The turtle drawing library is used to explain the logic of loops,
# while showing the features of the turtle drawing library.
#
# Uses turtle - a drawing library.
#
# Some methods to control turtle:
#  Reference Turtle Methods: http://interactivepython.org/runestone/static/IntroPythonTurtles/Summary/summary.html
#
#
# Tip: with pycharm, to prevent turtle from closing the window after execution,
#      add turtle.exitonclick(); and/or turtle.done()


# Example 1, drawing line, output with turtle.

import turtle

turtle.color('green')
turtle.forward(100)
turtle.right(45)
turtle.color('blue')
turtle.forward(50)
turtle.right(45)
turtle.color('pink')
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

#turtle.done()

import turtle
# For loop: for var in range(n)
# Add a square with turtle: using the for loop.
i = 0
turtle.color('blue')

# pen.up; pend.down fail...

for steps in range(4) :
    turtle.forward(90)
    turtle.right(90)
turtle.up
turtle.forward(90)
turtle.color('red')
turtle.down
turtle.forward(100)

turtle.shape('turtle')


# This is a sample of a nested loop
# The outer loop executes 4 times, for each iteration/execution: the inner loop executes an additional 4 times(16).
#
# 4x

# for steps in range(4):
#     turtle.forward(100)
#     turtle.right(90)
#     # iterations: steps * moresteps
#     for moresteps in range(4):
#         turtle.forward(50)
#         turtle.right(90)


# nested loop 5x5
# for steps in range(5):
#     turtle.forward(100)
#     turtle.right(360/5)
#     for moresteps in range(5):
#         turtle.forward(50)
#         turtle.right(360/5)

# nested loop 11x11
# for steps in range(11):
#     turtle.forward(100)
#     turtle.right(360/11)
#     for moresteps in range(11):
#         turtle.forward(50)
#         turtle.right(360/11)


for steps in range(4):
    turtle.forward(10)
    turtle.right(90)
    for stesp in range(4):
        turtle.forward(50)
        turtle.right(90)



turtle.done()


