#! /usr/bin/env python3
import sys

MEM_INFO_FILE = '/proc/meminfo'
MEM_INFO_DELIM = ':'


def main(args):
    mem_dict = dict()
    # Buil mem_dict from file
    with open(MEM_INFO_FILE) as f:
        for line in f.readlines():
            try:
                # get the key and value
                # (ie 'SwapFree:    1048752 KB' should be unpacked)

                # fill in this line

                # cleanup (strip) whitespaces and remove KB (only keep numbers)

                # fill in this line
            except:
                print('Could not read line' + line)

    sum_kb = 0
    for arg in args:
        try:
            sum_kb += int(mem_dict[arg])
        except:
            print('Unable to get value for arg' + arg)

    print('Total is ' + int(sum_kb))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1:])


# usage
# python3 proc_mem.py WritebackTmp CommitLimit
# Total is 272342

# Likely bugs in this implementation!  Just for a rough idea
