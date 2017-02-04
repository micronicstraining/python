#! /usr/bin/env python3
import pickle
import marshal

# Say we want to convert more complicated objects to data
# This process is known as serialization
# You can't encode certain things in Python into JSON.
# That is why sometimes its better ot use Pickling

# Read through https://docs.python.org/2/library/pickle.html#what-can-be-pickled-and-unpickled
# to see what types are supported for pickling

# sets, lists, tuples, dictionaries (with only picklable objects inside)
print(pickle.dumps({1,2,3}))
print(pickle.dumps([1,2,2,3,3,3,4]))
print(pickle.dumps((1,2,(3,4),(3,(5,5)))))
print(pickle.dumps({1:2, 3:(4,5)}))

# as you can see built in functions are supported
print(pickle.dumps(print))
print(pickle.dumps(sum))

# Picle converts python objects to binary data that can be stored
# or sent to another application/end system

# There are things that even pickle doesn't support
# For example functions are not built in aren't directly supported.

# In order to solve that problem we need to get the "code" object
# from the function and marshal that as a string.
def add_one(x):
    return x+1

# add_one is the name bound to the code object
# In order to access the inner code object use __code__
add_one.__code__

# We can marshal this raw data which is able to work with code objects
# and convert it to a stream of byte code.
# Now we can store it in a dictionary object.
D = {'add_one': marshal.dumps(add_one.__code__)}

# Now D is ready to be pickled.
d_serialized = pickle.dumps(D)

# What does this look like?
print(d_serialized)

# As you can see, pickling is actually a protocol based around
# storing and reading python byte-code.  If you think about it, how else
# would you represent python objects?

# Write the d_serialized data to FILE_NAME
FILE_NAME = 'serialization.pickle'
with open(FILE_NAME, mode='wb') as f:
    pickle.dump(d_serialized, f)

# we could also have sent it over the network to another host.
# This is one way to send objects over the line.

# Note we are using mode=wb which means write bytes
# See what happens if you remove it.
