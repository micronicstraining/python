#!/usr/bin/env python3
import sys
import subprocess


def ping(url, count):
    return subprocess.check_output(['ping', '-c', str(count), url])


def main(args):
    for url in args:
        print(ping(url, 1))


if __name__ == '__main__':
    main(sys.argv[1:])
