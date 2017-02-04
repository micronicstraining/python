#! /usr/bin/env python3
class Person:
    def __init__(self, name):
        self.name = name


    def __enter__(self):
        print('{0} is born'.format(self.name))


    def __exit__(self, exc_type, exc_val, exc_tb):
        print('{0} is dead'.format(self.name))


with Person(name="tigran") as person:
    # block of stuff
    print('He is alive for a while!')


