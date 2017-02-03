#! /usr/bin/env python3
import sys
import ip_module
import dns_module
import ftp_module
import user_module


def main(args):
    o1, o2, o3, o4 = ip_module.parse(args)


if __name__ == '__main__':
    main(sys.argv[1:])