# what will be the output?
a = 2
a = 4
a = 6
print(a+a+a)


# id is a built in function that can be thought of as
# getting the memory address of the object

# immutable objects cant change value
# mutable objects can
# is objects of type int immutable object?
# another way of asking is will any of the the 
# next statements ever be false?
id(1) == id(1)
a = 1
id(a) == id(1)
b = 1
id(a) == id(b)
b = 10
id(b) == id(10)

# what would happen if instead of integers we used strings in the previous example?
# Are strings immutable?
# How can you prove it?


# will the print statements be different?
a = 2
print(id(2))

# What does the following do? What is the value of a?
a = 6
a = a + a
a = a + a

# The += operator is a shorthand for a = a + something
# So the following is the same as the previous example
a = 6
a += a
a += a

# Arity means the number of inputs an operator or function takes

# what is the arity of the '+=' operator?

# what will be the output
b = 1
b += 2
b += 3
print(b)


# what will be the output
c = 0
c -= 10
c -= 20
print(c)


# Integer division and floating point division are different.
# // is the operator for integer division in python.
# Integer division truncates to lowest integer value
# what will be the output
b = 6
c = -30
c //= b
print(c)

# What will be the following output?
b = 6
c = -31
c //= b
print(c)

# what will be the output of the following
b = 5
c = - 30
c /= b
print(c)


b = 5.1
c = -30
c /= b

# what does the *= operator do?


# What is 5 ** 3?
# What does the **= operator do?

input_y = 15

# can you say what the output of the followin function will be
# given that only integer inputs
def some_function(input_x):
    input_y = 20
    return input_x ** input_x

def my_adder(x, y, z):
    return x + y + z

def average(my_list):
    return sum(my_list)/len(average)

# what will be the output of the following given integer inputs
def zero_identity(x):
    return x * 0

some_function(5)

# what if we pass in floating points?  Is it possible to get a non-zero output?
# replace the 0 with something to get a non-zero result
how_can_we_break_zero_identity = 0
zero_identity(how_can_we_break_zero_identity)
