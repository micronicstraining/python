# Exploring functions
#
# Type the following canonical first program into the Python 3
# >>> print('Hello World!')
# What is the output?

# Print is a built-in function.
# Functions are called by putting parenthesis after them.
# If x is a function, x() calls or executes the function x.

# Putting single quotes around something means you are creating a literal string
# Type in
# >>> 'Hello World'
# What is the output
# type in
# >>> type('Hello World')
# This shows
# Get help on it by typing the following:
# >>> help(print)

# Type in 5
# >>> 5
# What is the output
# Can you print 5 without quotes?
# >>> print(5)
# What does this imply?


# It basically means print supports different types of objects


# Notice how in the help it had a '...'
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
#

# help, explore keywords, modules,


# Exploring python objects (SKIP THIS FOR NOW, WILL BE MOVED TO LATER SECTION)

# Read the following summary and do the exercises.
#
# SUMMARY start:
#
# Python objects, values types
#
# Axioms for Python objects
# 0) Objects are Python’s abstraction for data
#       Objects "contain" other objects
#       Objects "box" or "contain" a value
#       A value is the raw data itself
# 1) Python VM operates on a stack of Python objects
#       Python's VM can't operate on raw data, only objects.
# 2) Every object contains a value, a type, and an id.
#       Think of id as an integer object with a raw value of a memory address.
#       Once an object is created it stays at a certain address.
#       The id of an object is not changeable.
# 3) Objects have values that are either changeable or not changeable.
#       If they are not changeable they are called immutable
#       If they are changeable they are called mutable
# 4) All objects inherit from a base object called 'object'
#
# There are three categories of types:
# 1) Built-in types:
#    none, numerics, sequences, mappings, files, functions,
#    classes, instances and exceptions.
# 2) User-defined types:
#    Custom classes and modules not in the standard library
#    You create these with the class keyword
#    ie:
#    class Person:
#        ...
#
# 3) Meta-class types:
#    Classes that create classes.
#    Imagine a machine, other than you, that creates a class.
# 3) All types have a base type 'type'.
#    In a sense type if an instance of itself.
#    Note: Type checking is done with the 'is' built-in operator
#    >>> type(type)
#    <class 'type'>
#    >>> type(type) is type
#    >>> True
#
# Summary end
#

