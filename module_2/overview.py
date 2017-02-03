#! /usr/bin/env python3

# nonetype
none_object = None

# bools
bool_object_true = True
bool_object_false = False

# if False:
#     print('This is a basic if branch')
# elif True:
#     print('This is a basic else if branch')
# else:
#     print('this is a basic else branch')

bool_not_example = not True
print(bool_not_example)

bool_and_example = True and True

# a    b    |    a    and     b
# F    F    |          F
# F    T    |          F
# T    F    |          F
# T    T    |          T

bool_or_example = False or False
# a    b    |    a    or     b
# F    F    |          F
# F    T    |          T
# T    F    |          T
# T    T    |          T


# integers - integral types
int_5 = 5
int_neg_5 = -5


# strings
# collections
# sequences  &  non-sequence (ordered?)
# immutable vs mutable?
print('This is a sentence in unicode! ' + 'I ❤ Unicode')

x = 'This is a sentence.  This is another sentence'
print(x[0])
print(x[1])
print(len(x))
print(x[17])
print(x[len(x)-1])
print(x[-2])

print(x[0:4])
print(x[0:3])

print('0123456789'[2:-2])

print(x.split(' '))
print(x.split('.')[0])


# list
my_list = [None, True, False, 'hello', 5, 13+4, [1,2,3, [1,2,3]]]
my_list.append('hello world')
print(id(my_list))
print(my_list)
my_list.append(2**10)
print(my_list)
print(id(my_list))
print(type(my_list))

# for mutable types, this list will be copied
my_list2 = my_list[:]
print(id(my_list))
print(id(my_list2))
my_list.append('something else')
print(my_list2)

# merge lists
list1 = [1,2,3]
list2 = [3,4,5]
list3 = list1 + list2
print(list3)

# slices lists
print(list3[1:-1:2])

for e in list3:
    print(e, e**2)

# tuple
tuple1 = (1,2,3)
tuple2 = (3,4,5)
tuple3 = tuple1 + tuple2

print(tuple3)
print(type(tuple3))

lat_long = (34.1234, -74.2342)
print(lat_long[0])
print(lat_long[1])

lat1, long1 = (32.234234, -70.23423)
print(lat1)
print(long1)

lat1, *_ = (32.23423, -70.234234, 12342)
print(lat1)
print(_)

# zip- built in function
l1 = [0,1,2]
l2 = ['a','b','c']
print(list(zip(l1, l2)))

for index, letter in enumerate(l2):
    print(index, letter)


# set
# unordered = not sequence
# collection
#

# lists - mutable
[]

# problems with mutability
a = [1,2,3]
b = a
a.append(4)
# now b is also 1,2,3,4!
# How can we copy the list a to b ?

# tuples - immutable
()

# sets - mutable - unordered
{1, 2, 3}

# dictionaries (keys, value) - mutable - unordered
dict1 = {
    'hello': 'a',
    'goodbye': 'b',
    'test': 'c'
}

print(dict1['hello'])
print(dict1['goodbye'])
print(dict1['test'])

a = dict(one=1, two=2, three=3)

b = {'one': 1, 'two': 2, 'three': 3}

c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))

d = dict([('two', 2), ('one', 1), ('three', 3)])

# should be true
assert (a == b == c == d)

