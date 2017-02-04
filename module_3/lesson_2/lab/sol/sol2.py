#! /usr/bin/env python3

# Create a Person class
# It should have a first name, last name and age.
# It should receive these values through the constructor.
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
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.file_name = Person.__name__ + '.' +  str(id(self)) + '.pickle'

    def pickle(self):
         with open(self.file_name, mode="wb") as f:
             d = pickle.dump(self, f)


def main():
    me = Person(first="Tigran",last="Avakyan",age=31)
    me.pickle()


if __name__ == '__main__':
    main()
