letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# Access elements can be done by playing a brackets in front of letters
# ie letters[some_index_number_goes_here]
# How can we output the 2nd letter?


# How can we output the 5th letter?


# Name some possible motivations for writing the following line of code
# Is there an error or mistake? 
letters[len(letters)]

# How we can output the last letter?


# Is there another more idiomatic way to output the last letter?


# What will the following code do
i = len(letters)
letters.append('k')
print(letters[i])

# What does this output?
letters[0:3]

# What does it mean to say that slicing is upper-bound exclusive and lower-bound inclusive?


# How can we output a slice of all but the outtermost letters?


# How can we output a slice of the last 3 letters?


# What does the following do?
letters[0:-1:2]


# How do you access all the odd elements in letters?



# Here is an example of a lambda function named f.
f = lambda i, x: x[i] if 0 < i <= len(x) else 0

# This function returns the ith element in x if within the size of the list
# Otherwise, it returns  returns 0.
# For example.  To call it you do:
# f(2, letters)
# >> 'c'
# f(-15, letters)
# >> 0

# What does the following lambda function g do?
g = lambda i, x: x[i] if 0 <= i < len(x) else ( x[0] if i < 0 else x[-1] )
# What is g(-15, letters)?
# What is g(500, letters)?

