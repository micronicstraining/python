#!/usr/bin/env python3
import sys
import subprocess


def ping_count(url, count=1):
    return subprocess.check_output(['ping', '-c', str(count), url])


def main(args):
    # args == urls (supposed to be)
    output = []
    for url in args:
        output.append(ping_count(url))
    print(output)


if __name__ == '__main__':
    main(sys.argv[1:])


# Step 1
# Make this script ping multiple hosts:
# ie
# ./ping_all.py www.google.com www.yahoo.com
#
#
# Step 2
# Copy first script, create a ping_all_s2.py
# Use argparse to parse a 'count' parameter as well as URL list
# See: https://docs.python.org/3.6/library/argparse.html
# ie get the following to work:
# ./ping_all_s2.py --count 3 --urls www.google.com www.yahoo.com www.bing.com
#
# HINT: Use type=str, nargs='+' for --urls
#

