# File: loopsCounting.py
# Description: Example of utilizing values within loops.
#

import turtle
for step in range(4):
    print(step)


# Range validation
# (min, max, increment)
for steps in range(1,10,2):
    print(steps)

# list values specified with brackets []
for steps in [1,2,3,4,5] :
    print(steps)

# Loop values not confined to numbers.
for color in ['red', 'blue', 'green', 'pink', 'black'] :
    turtle.color(steps)
    turtle.forward(100)
    turtle.right(72)


for color in ['red', 'green', 'blue', 'black'] :
    turtle.color(color)
    turtle.forward(100)
    turtle.left(72)

turtle.done()

