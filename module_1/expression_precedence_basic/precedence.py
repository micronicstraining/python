# We will use assert to see whether compound expressions are evaluated
# to a corresponding simpler form.
# Also the '==' means are the two statements equivalent in value?


# This is how you ask 'Is 1 equal to 2?' in python.
# The answer is obviously no so the assert below will raise an exception.
# (note: exceptions interrupt of execution and stop program from running)
# assert(1==2)

# Is 2 equal to 2? Should be safe.
assert(2==2)

# Is 2 * 2 * 2 equal to 8? Should be safe.
assert(2*2*2 == 8)

# ... another way to write 2^3 equal to 8?
assert(2**3 == 8)

# If you uncomment the next line of code will it raise an exception?
# assert( 2 - 3 * 5 == -5)

# What about now?
# assert( (2-3) * 5 == -5)

# What should x be equal to in order to not cause an exception?
# x = ?
# assert( 2 * 5 ** 2 == x)

