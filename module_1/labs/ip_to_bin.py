#!/usr/bin/env python3
import sys


def main(ip_address):
    pass
    # split ip address to octets

    # Ensure we have 4 octets

    # Try to print the octets in binary format
    # Use a loop iterating through octets and printing
    # their binary values


if __name__ == '__main__':
    if len(sys.argv) == 2:
        # Pass second argument to script
        # which should be the IP address
        main(sys.argv[1])


# Example usage:
#
# ./ip_to_bin.py 192.168.20.14
# 0b11000000
# 0b10101000
# 0b10100
# 0b1110
