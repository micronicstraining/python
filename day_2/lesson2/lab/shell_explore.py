import sys
import crypt
DICT_FILE = '/usr/share/dict/words.short'
def main(arg):
    salt = '$6$Mqe5XrQt'
    hashed_pass = arg

    with open(DICT_FILE) as f:
        for line in reversed(f.readlines()):
            line = line.strip()
            print(line)
            print(salt)
            print(hashed_pass == """$6$Mqe5XrQt$4Y34YRjp5bD/3ROR9OnwrFSqKurE7WvmpZGkkmIvwVHaFSH802PwaC0ViMMKQDvFhWtDRx2RSm8tQv6rj5E9B1""")
            if crypt.crypt(hashed_pass, salt) == hashed_pass:
                print(line)

if __name__ == '__main__':
    main(sys.argv[1])

# DO THIS LAB:
# ./shell_explore.py $6$Mqe5XrQt$4Y34YRjp5bD/3ROR9OnwrFSqKurE7WvmpZGkkmIvwVHaFSH802PwaC0ViMMKQDvFhWtDRx2RSm8tQv6rj5E9B1
# vagrant
# Lab:
# ﻿sudo cat /etc/shadow - what is this thing?
#
# ﻿cat /usr/share/dict/words
#
# ﻿cat /usr/share/dict/words | grep vagrant
#
# the $6$ means sha 512 encryption (hash)
# the salt is $6$Mqe5XrQt (up to but not including $)
#
# the rest of the code:
# 4Y34YRjp5bD/3ROR9OnwrFSqKurE7WvmpZGkkmIvwVHaFSH802PwaC0ViMMKQDvFhWtDRx2RSm8tQv6rj5E9B1

# ... is the encrypted password


# create a brute forcer that uses
# /usr/share/dict/words
# where you input the salt
# adn the encrypted password into args
# and it iterates through all words until it matches

# not use crypt library
# import crypt
#
# in ordre to encrypt we do:
# crypt.crypt(dictionary_word, salt)
