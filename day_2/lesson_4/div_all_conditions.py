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
INVALID_NUMBER_OF_INPUTS = 5

def main(args):
    # unpack the tuple
    num, den = args
    try:
        # cast to floating point
        num, den = float(num), float(den)
    # what type of exception if cast doesn't work?
    # ie try float('a') in our python3 shell
    except ValueError as e:
        # is this an error or a warning?
        logging.error('Invalid input. Could not convert input to decimal')
        return INVALID_INPUT

    # if denominator is equal zero
    if den == 0:
        # is this a warning or error?
        logging.warning('Invalid denominator input!')
        return DIV_BY_ZERO_EXIT

    # if numerator or denominator is nan?
    if math.isnan(den) or math.isnan(num):
        logging.warning('Nan in den or num')
        return INVALID_INPUT_NAN

    # if numerator or denominator is inf?
    if math.isinf(den) or math.isinf(num):
        logging.warn(('Inf input in den or num'))
        return INVALID_INPUT_INF

    print('Answer: ' + str(num / den))
    return 0


if __name__ == '__main__':
    status = INVALID_NUMBER_OF_INPUTS
    if len(sys.argv) == 3:
        status = main(sys.argv[1:])
    sys.exit(status)
