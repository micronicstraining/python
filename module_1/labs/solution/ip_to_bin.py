#!/usr/bin/env python3
import sys


def main(ip_address):
    octets = ip_address.split('.')

    # Ensure we have 4 octets
    if len(octets) != 4:
        print("Invalid IPv4 address format")
        return

    # Try to print the octets in binary format
    for octet in octets:
        try:
            print(bin(int(octet)))
        except ValueError:
            print("Cannot convert IPv4 address to an integer")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        # Pass second argument to script
        # which should be the IP address
        main(sys.argv[1])
