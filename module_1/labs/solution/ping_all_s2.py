#!/usr/bin/env python3
import sys
import subprocess
import argparse


def ping(url, count):
    return subprocess.check_output(['ping', '-c', str(count), url])


def main(args):
    parser = argparse.ArgumentParser(description='Ping URLs with count param.')

    parser.add_argument('--urls', type=str, nargs='+', help='list of URLs')
    parser.add_argument('--count', default=1, help='Set count of pings')

    args = parser.parse_args(args)
    for url in args.urls:
        print(ping(url, args.count))


if __name__ == '__main__':
    main(sys.argv[1:])
