#! /usr/bin/env python3
# Create a simple divide program that takes in two floats
# ie
# ./div_all_conditions 1 2
# 0.5
# It should handle non string inputs, zero denomintor and inf and nan
# inf is a floating point which is an infinity
# nan is a floating poitn which is not a number
# user math.isinf and math.isnan functions to check for this
# user logging to register warnings and errors
# return the global flags following the imports if anything goes wrong
import sys
import logging
import math


INVALID_INPUT = 1
DIV_BY_ZERO_EXIT = 2
INVALID_INPUT_NAN = 3
INVALID_INPUT_INF = 4


def main(args):
    # unpack the tuple
    # num, den = ?
    try:
        # cast to floating point
        # num, den = ?, ?
    # what type of exception if cast doesn't work?
    # ie try float('a') in our python3 shell
    except ? as e:
        # is this an error or a warning?
        logging.?('Invalid input')
        return ?

    # if denmonitor is zero
    if ? == ?:
        # is this a warning or error?
        logging.?('Invalid denominator input!')
        return ?

    # if numerator or denominator is nan?
    if ?:
        return ?

    # if numerator or denominator is inf?
    if ?:
        return ?

    print('Answer: ' + str(num / den))
    return 0


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[1:])
