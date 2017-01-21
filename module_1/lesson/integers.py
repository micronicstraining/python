# Follow this to tutorial learn about integers in Python


# One of the build-in types of python which supports 'literal' is an integer
# A literal means you can 'literally' type in the raw value directly
# For example, type in 5 into the python shell
# >>> 5
# 5

# What will be the output if you type 5+5?


# Since everything is an object there is a non-literal form
# Type int(5) into the python shell.  What is the output?
# >>> int(5)
# ?


# This is how the literal '5' is 'boxed' into an object.
# Another way to think of it is:
# There is an object of type integer with the value of 5


# What is the memory address or id of the number 5?
# Use the builtin id function to get the address
# ?

# What is the memory address if you use the non-literal form: int(5)
# ?


# If you make x = 5 and y = x what will be the id of x & y?



# If you make x = int(5) and y = int(5) what will be the id of x & y?



# Integers have a value basic operators you can apply like
#   addition +
#   subtraction -
#   division /
#   integer division //
#   multiplication *
#   power/exponent **  ie 2 ^ 10 = 1024
#   modulus %   1024 % 100 == 24, 5 % 2 == 1,  10 % 2 == 0
#
# These operators have an arity of 2 meaning they take 2 inputs
# For example x = 5 + 5
#
# Solve the following problems using these operators:


# Use module to determine whether a number is even.  It should work with any integer.

# In many languages integers have a minimum and maximum value.
# This is not the case in Python and the limitation is only memory.
# Integers are unlimited in size and have no maximum value in Python.
# To prove this do the following
# import sys and print out the variable sys.maxsize
# Assign a value to it and increment the value
# In other languages you would get an overflow and
# it would give you the largest negative.
# Python adjusts acccording to the integer size you need.
# To prove this try to to multiply sys.maxsize by itself?
# Note: the multiply operator
# Now try to
