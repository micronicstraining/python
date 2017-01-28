#! /usr/bin/env python3
# Create a package with two modules
# Make sure the package has a side-effect, such as a print statement in the __init__.py
# import both those modules here and execute the program
# Does the side-effect occur once or twice?
import sys

if __name__ == '__main__':
    print('Hello from 04_package_experiment')
    print('These are the imported modules: ')
    print(sys.modules.keys())


# Read this:
# http://stackoverflow.com/questions/296036/does-python-optimize-modules-when-they-are-imported-multiple-times#296062


# my example:
# from package_with_side_effect_2 import mod_1
# from package_with_side_effect_2 import mod_2
#
# if __name__ == '__main__':
#     print('hi')
