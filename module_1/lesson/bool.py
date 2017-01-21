# A bool or a boolean expression has two values: True and False
# Booleans can be thought of in at least two ways:
#    Sentences or statements that are propositions (and either true or false)
#    Information that is either 0 or 1.  A single bit.

# Input a literal True into the Python3 shell
# >>> True
# True

# Do the same with False

# The REPL knows these are built in keywords.
# Try to make a variable name True that is equal to None
# >>> True = None
# What happens?
# No variables can be named True or False


# The equal to operator, which checks to see if things are equal, returns a bool
# >>> None == None
# True
# >>> True == True
# True
# >>> False == False
# True
# >>> True == False
# False
# >>> False == True
# False

# x = 5
# x == 5
# result = x == 5
# print(result)

# What is the arity of the comparison operator?

# Note the comparison operator doesn't only take bools as inputs!
# Try the following
# >>> None == True
# >>> None == False
# >>> None == None

# If you do have bools on both sides, then its like a compound boolean expression.

# The equal to operator has a dual operator called not equal to: !=
# What will be the output of the following?
# >>> True != True
# >>> True != False
# >>> (False == True) != False

# Bools have certain operations that are supported such as:
# not
# and
# or

# not has an arity of 1 meaning it only takes one input:
# >>> not False
# >>> not True
# >>> f = not True
# >>> t = not False
# As you can see it just negates the value

# This is the truth table for not:
# a       |   not a
# False   |   True
# True    |   False

# You can compose Not together as follows:
# >>> not not True
# >>> not (not True)
# >>> not not False
# >>> not (not False)
# Here the parenthesis mean do this operation first.
# Both cases do the inner (to the rightmost) operation first,
# but parenthesis can add clarity
# >>> not (not (not (True)))

# What would happen if you did the not of None?

# What will be the result of teh following operation?
# >>> not True == False

# What has a higher precedence not or ==?  Ie what gets evaluated first?
# How can you force a difference precedence?  Show an example
# will the output be the same in this case?

# You can create larger comparison chains and they get calculated from left to right
# >>> False == True == False == True == False
# False

# the and operator takes two inputs so its has an arity of 2.
# and operation is True if and only if both inputs are true, otherwise false
# The following is the truth table for and:
#   a   |     b    |    a and b
# False |   False  |    False
# False |   True   |    False
# True  |   False  |    False
# True  |   True   |    True

# Question.  If 2 inputs create 4 possible rows in a truth table
# then how many rows will you have with 3 inputs? What about with 4 and 5?

# Question: If you have a type that supported 3 options:
# State A, State B, State C
# And there was an operator called 'next' with an arity of 1
# which goes to the next state as follows:
# A -> B -> C -> A ...
# How many combinations can be made with 2 variables?
# Ie how many rows in the table.


# Finish the following truth table:
# x        |       y
# A        |       A
# A        |       B
#         ...


# The or operator returns False only when both inputs are false.
# Write out the truth table for or:


# Problem:
# Convert this statement into a logical expression:
# A switch is either closed (letting electricity pass in) or open (not letting electricity pass)
# I have 4 switches which open a door named a, b, c, d
# a and b are connected in series ( that means one after another, meaning both must be closed)
# c and d are connected in parallel ( at least one has to be on)
# the output of both of those is connected in parallel
# all switches are set to off in the beginning
#
# ie give the answer in the following form:
# >>> a, b, c, d = False, False, False, False
# >>> door_open = a and b or (c and not d)
# I have four switches a, b, c, and d that will either open a door or leave it closed.
# a and b are connected in series (after each other so both need to be


# Look up Demorgan's theorem on wikipedia and test it out with
# python expressions

# use demorgan's theorem to simplify the following expression:
# not ( not a or not b )


# There is no operator for exclusive or
# Exclusive or has an arity of 2 and is True if there is at least one True
#
# Problem
# Write out the truth table for exclusive or
#
# Problem
# write out an expression given a and b that uses or, and and not to do exclusive or

# if statements basic
# if statements take in a boolean and if the bool is truth they change the flow
# of control (they branch) to another block of code:

# Type the following into the shell:
# if True: print('this should run')

# What would be the result if you put False instead of True?

# Booleans can be polymorphic to numbers
# What would happen if you did the following:
# >>> True * False
# >>> True + True + False + False
# >>> True + 5
# >>> False - 1

# Notice how True and False get converted to 1 and 0
