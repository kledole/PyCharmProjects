# File geometry.py
# Description: The following program prompts the user
# to enter the number of shape sides.  (from 3 to 18).
# 18 is set to limit for the turtle default screen and output.
#
# The program will then draw an object with the number
# of sides specified by the user.
#
# Uses turtle drawing library.

import turtle

print('The following program will print out a geometric shape.')
print('The object will have 3-360 sides, based on your input.')

num_sides = input('Please enter the number of sides for the object: from 3 to 18')
num_sides = int(num_sides)

while num_sides < 3 or num_sides > 19:
    num_sides = input('{0:d} Please enter a number between 3 and 18.'.format(int(num_sides)))
    num_sides = int(num_sides)


print(num_sides)

turtle.color('black')

for steps in range(num_sides) :
    turtle.forward(50)
    turtle.right(360/num_sides)

turtle.penup()
turtle.right(25)
turtle.forward(25)
turtle.pendown()
for steps in range(num_sides) :
    turtle.forward(10)
    turtle.right(360/num_sides)


turtle.done()

