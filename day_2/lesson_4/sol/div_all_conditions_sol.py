#! /usr/bin/env python3
import sys
import logging
import math


INVALID_INPUT = 1
DIV_BY_ZERO_EXIT = 2
INVALID_INPUT_NAN = 3
INVALID_INPUT_INF = 4


def main(args):
    num, den = args
    try:
        num, den = float(num), float(den)
    except ValueError as e:
        logging.error('Invalid input')
        return INVALID_INPUT

    if den == 0:
        # this is a run-time error but not a type error
        # can be considered a warning or an error based on use case
        # written here as mere warning.
        logging.warn('Invalid denominator input!')
        return DIV_BY_ZERO_EXIT

    if math.isnan(num) or math.isnan(den):
        return INVALID_INPUT_NAN

    if math.isinf(num) or math.isinf(den):
        return INVALID_INPUT_INF

    print('Answer: ' + str(num / den))
    return 0


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[1:])
