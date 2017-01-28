#!/usr/bin/env python3
import sys


def main(ip_address):

    # split ip address to octets
    octets = ip_address.split('.')

    # Ensure we have 4 octets
    if len(octets) != 4:
        return

    # Try to print the octets in binary format
    # Use a loop iterating through octets and printing
    # their binary values
    try:
        for octet in octets:
            print(bin(int(octet)))
    except ValueError:
        print('Value error!  Unable to convert octet string to integer')



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
