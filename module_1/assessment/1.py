# what will be the output
a = 2
a = 4
a = 6
print(a+a+a)


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



# what will be the output
c //= b
print(c)


# what will be the output of the following
c = - 30
c /= b
print(c)


# can you say what the output of the followin function will be
# given that only integer inputs
def some_function(input_x):
    return input_x ** input_x


# what will be the output of the following given integer inputs
def zero_identity(x):
    return x * 0


# what if we pass in floating points?  Is it possible to get a non-zero output?
# replace the 0 with something to get a non-zero result
how_can_we_break_zero_identity = 0
zero_identity(how_can_we_break_zero_identity)
