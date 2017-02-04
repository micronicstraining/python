# Create a rotate by 13 encoder - http://www.rot13.com/
# Use:
# hint use codecs.encode.  look it up in the documentation
def rot13_encode(data):
    """ Take in unencoded data and rot13 and return new data """
    pass

# What will be the output?
# hello_world_rotated = rot13_encode("Hello World")
# print(hello_world_rotated)


# Reverse a string using a slice
# use [::-1]

# Reverse a string using resversed keyword
# >>> reversed('hello')
# <reversed object at 0x10a833898>
# >>> ''.join(reversed('hello'))
# 'olleh''

# Between last two which is more 'pythonic'?


# What is wrong with the following code:
# >>> (1,2) + (1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate tuple (not "int") to tuple
# Note: the intent is to concat to the first tuple
# How can you fix it?

# Create a dictionary with the country followed by it's capital city
# for the following countries:
# China, Germany, Greece, Russia, United Kingdom

# Print out only the values

# >>> ord('A')
# 65
# ord('A') - ord('\0') 
# 65

# What do you think ord does?  Can you apply it to a list in a loop?

# Can you apply it using a map?
# >>> list(map(ord, 'Hello'))
# [72, 101, 108, 108, 111]
# >>>

# What if ou had a word and you wanted to convert it to a stream of bits
# How can you do this using ordinal and map?
# >>> list(map(bin, map(ord, 'Hello')))
# ['0b1001000', '0b1100101', '0b1101100', '0b1101100', '0b1101111']

# datetime practice
# from datetime import datetime
# how can you get current time?

# how can you calculate number of days since your birthday?

# hackerrank datetime problems

# In order to send email you can use the send-mail transfer protocol (SMTP)
# there is a built-in library for this
# What do you think the following code does:
# >>> import smtplib
# >>> s = smtplib.SMTP('localhost', 1025)
# >>> s.sendmail('me@example.com', 'you@example.com', "Python is awesome!")
# Open wireshark and start capturing
# Create a script with above and launch it with:
# python -m smtpd -n -c DebuggingServer localhost:1025
# See if you can find SMTP packet sent

# syslogd is
# a socket is a TCP or UDP connection to an ip address/port which lets you
# send and recieve data
# what do ou think the following code does?
# >>> from socket import *
# >>> syslogd = socket(AF_INET, SOCK_DGRAM)
# >>> syslogd.bind(('localhost', 514))
# >>> while True:
# ...     message, source = syslogd.recvfrom(2048)
# ...     print "[%s] %s" % (source[0], message)
#

# Create a class called Address
# It hsould have a line 1, line 2, city, state, zip, country
# over ride the __repr__ to print out a well formatted address.
#
# Create a class call Customer
# It should have a first name, last name, email and address object
#
# SKIP NEXT ONE:
# Create a product class.  It hsould have an item name and cost.
# Override the __add__ method so products can be added to each other
#
# - closure, lambda review
#
