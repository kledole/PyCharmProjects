# File: numbers.py
#
# Description: Basic intro to numeric functions
#   - using numbers and numeric functions in Python
#
# Symbols   Operation    Examples:
#
# +         Addition    8 + 2
# -         Subtraction  5-2
# *         Multiplication 4 * 4
# **        Exponent       2** = 4
# %         Modulo          5%2 = 1


# formatting values
#  %d decimal
# %3d
# %f - float
# %.2f




# init
area = 0
height = 10
width = 20

# Print area of triangle
area = width * height / 2

# Use of % and format strings in print statement to display number

print('The area of the triangle is: %.2f ' % area)


print("My favorite number is %d" % 42)

# print right justified with 6 zeros.
print("My favorite number is %06d" % 42)

# Different syntax: {n:<format>}
# {0:d}, {0:3d}, (0:03d}, {o:f}, {0:.2f}
print("format(6,2) and format(6) examples.")
print("{0:d}:")
print("I have {0:d} cats.".format(6,2))
print("{1:d}:")
print("I have {1:d} cats.".format(6,2))
print("{0:3d}:")
print("I have {0:3d} cats.".format(6))
print("{0:03d}:")
print("I have {0:03d} cats.".format(6))
print("{0:f}:")
print("I have {0:f} cats.".format(6))
print("{0:.2f}:")
print("I have {0:.2f} cats.".format(6))

print("The area of the triangle would be {0:f}format(area)")
print("My favorite number is {0:d} ".format(42))

print('Here are three numbers! \n \
The first number is {0:d}. \n \
The second number is {1:4d}. \n \
The third number is {2:d}.'.format(7,8,9))



