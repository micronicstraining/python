letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# Access elements can be done by playing a brackets in front of letters
# ie letters[some_index_number_goes_here]
# How can we output the 2nd letter?


# How can we output the 5th letter?


# In order to get the number of elements in a list you can use len
# ie length = len(letters) 
# will make length == 10


# Name some possible motivations for writing the following line of code
# Is there an error or mistake? 
letters[len(letters)]

# How we can output the last letter?


# Is there another more idiomatic way to output the last letter?
# Hint what happens when you put a negative number as the index?

# What will the following code do?
# What does append mean? 
i = len(letters)
letters.append('k')
print(letters[i])

# Slicing gives a subset of a list can be done as follows:
# letters[lower_element, upper_element_excluded]
# The following is an example of slicing an array.  What does it output?
letters[0:3]

# What if we omit the first index?  What does this output?
letters[:3]

# What does it mean to say that slicing is upper-bound exclusive and lower-bound inclusive?


# How can we output a slice of all but the outtermost letters?


# The complete syntax of list slicing is [start:end:step] . 
# When you don't pass a step, Python assumes the step is 1.
# [:]  itself means get everything from start to end. 
# [::2]  means get everything from start to end at a step of two
# How would you get every 3rd element starting from the 2nd and going
# all the way to, but not including, the second to last element?
# Hint: the output should be ['b', 'e', 'h']


# How can we output a slice of the last 3 letters?
# Hint: # when you don't put index to the right of the colon what happens?

# Is the following statement true? Why or why not?
letters[0:-1:2] == letters[::2]


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

