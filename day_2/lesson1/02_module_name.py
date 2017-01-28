#! /usr/bin/env python3
# How importing modules work
# what value is __name__ after import

import some_module_1
from some_package import some_module_2
from some_package.some_package_2 import some_module_3 as m3  # alias
import some_package.some_package_2.some_package_3.some_module_4 as m4 # alias


if __name__ == '__main__':
    print(some_module_1.__name__)
    print(some_module_2.__name__)
    print(m3.__name__)
    print(m4.__name__)
    print(__name__)  # what happens in the shell?
