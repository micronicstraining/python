#! /usr/bin/env python3

# Create a Person class
# It should have a first name, last name and age.
# It should recieve these values through the constuctor.
# It it should have a method called pickle with no inputs and no outputs
# That method should pickle that instance and store it in a file.
# The file name should have the following format:
# Person.102342342.pickle
#    where Person is the classname
#    102342342 is the id of the instance
#    .pickle is the extension of the file
#
# Create an instance of your Person object in main
# with your own first name, last name and age.
# Call pickle on it and ensure a file is created as expected.

import pickle


class Person():
    pass


def main():
    me = Person(first="Your first name",last="Your last name",age='your age')
    me.pickle()


if __name__ == '__main__':
    main()
