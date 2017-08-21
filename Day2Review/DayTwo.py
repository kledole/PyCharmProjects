# File: fileAccess.py
# Description: resuming review of python programming
#
# Prior exercises covered:
#  - hello world, basic theories about coding and practices for
#   - displaying text
#   - strings and variables
#   - numeric values, functions and comparisons
#   - date and time formatting and output
#   - conditional statements (if, elif, else, and, or), and more complex
#     comparisons and variations
#
# Day2 Begins at: 5:58:06

# References at:
# http://aka.ms/introprog-python
# http://aka.ms/intropythoncode

# Day2 will review the following concepts:
#  - Repeating events
#  - repeating events until done
#  - remembering lists
#  - methods to save information in files
#  - Reading from Files
#  - Functions
#  - Error Handling


# Uses turtle - a drawing library.
#
# Some methods to control turtle:
#  Reference Turtle Methods: http://interactivepython.org/runestone/static/IntroPythonTurtles/Summary/summary.html
#
#
# Tip: with pycharm, to prevent turtle from closing the window after execution,
#      add turtle.exitonclick()

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
turtle.forward(200)

turtle.shape('turtle')
turtle.done()


