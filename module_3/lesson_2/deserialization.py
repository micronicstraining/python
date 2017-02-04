#! /usr/bin/env python3
# see https://wiki.python.org/moin/UsingPickle
# and http://stackoverflow.com/questions/1253528/is-there-an-easy-way-to-pickle-a-python-function-or-otherwise-serialize-its-cod

import pickle
import marshal, types

FILE_NAME = 'serialization.pickle'

d = pickle.load(open(FILE_NAME, mode="rb"))
D = pickle.loads(d)

print(D)

code = marshal.loads(D['add_one'])
add_one = types.FunctionType(code, globals(), "add_one")

print(add_one(5))
