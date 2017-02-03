#! /usr/bin/env python3
import sys

MEM_INFO_FILE = '/proc/meminfo'
MEM_INFO_DELIM = ':'


def main(args):
    mem_dict = dict()
    # Build mem_dict from file
    with open(MEM_INFO_FILE) as f:
        for line in f.readlines():
            try:
                # get the key and value
                k, v = line.split(MEM_INFO_DELIM)
                k = k.strip()
                # Split between number and KB and keep only number
                v = v.strip().split(' ')[0]

                # insert into dictionary
                mem_dict[k] = v
            except:
                print('Could not read line' + line)

    # print(mem_dict)
    sum_kb = 0
    for input_key in args:
        try:
            sum_kb += int(mem_dict[input_key])
        except:
            print('Unable to get value for arg' + input_key)

    print('Total is ' + str(sum_kb))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1:])


# usage
# python3 proc_mem.py WritebackTmp CommitLimit
# Total is 272342

# Likely bugs in this implementation!  Just for a rough idea
