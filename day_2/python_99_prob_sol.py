# Solutions to
# https://sites.google.com/site/prologsite/prolog-problems/1

# 1.01 (*) Find the last element of a list.
l = [1,'test',(1,2,3),5,3,True,False,None,object,0,15,12]

last_elem = l[len(l)-1]
# or more pythonic:
last_elem = l[-1]


# 1.02 (*) Find the last but one element of a list.
second_to_last_elem = l[-2]


# 1.03 (*) Find the K'th element of a list.
def kth_elem(k, l):
    if k < len(l):
        return l[k]
    return None

# 1.04 (*) Find the number of elements of a list.
num_elements = len(l)


# 1.05 (*) Reverse a list.l
reverse_l = l[::-1]


# 1.06 (*) Find out whether a list is a palindrome.
def is_palindrome(l):
    # get length of list
    n = len(l)

    # iterate through index and element
    for i, e in enumerate(l):
        if e != l[n-i-1]:
            return False
        return True

# explaination of above
# given a list you need to compare the leftmost and rightmost
# elements while iterating through the loop
# ie l=[1,2,3,3,2,1], first compare l[0] to l[-1],
# then l[1] to l[-2]...
# If they are not equal then its not a palindrome
#

# solution using slices
def is_palindrom(l):
    if l == l[::-1]:
        return True
    return False

# 1.07 (**) Flatten a nested list structure.
l = [1, 2, [1,3,4, [5, 6], 2, [2,[3,4]]],[[[[[4,5]]]],6]]
l = [1,2,[3,4]]

# Note 1: in order to merge lists you can do
# [1,2,3] + [3,4,5] => [1,2,3,3,4,5]

# Note 2:
# two ways to check instance
# isinstance(l, list)
# or
# type(l)==list

def flatten(l):
    # return empty list if 0 elements
    if len(l) == 0:
        return []
    # if 1 element...
    elif len(l) == 1:
        # flatten if list ...
        if isinstance(l[0], list):
            return flatten(l[0])
        # or just return it
        else:
            return l
    # if more than 1 element ...
    else:
        # if first is a list flatten both sides ...
        if isinstance(l[0], list):
            return flatten(l[0]) + flatten(l[1:])
        # otherwise flatten only right side.
        else:
            return [l[0]]+ flatten(l[1:])


# 1.08 (**) Eliminate consecutive duplicates of list elements.
l = [1,2,3,3,2,4,2,3,5,6]

l_enumerate = enumerate(l)

# skip first element
next(l_enumerate)

l2 = []
for index, e in l_enumerate:
    # if consecutive duplicate, skip ...
    if l[index-1] == e:
        continue
    # otherwise append to l2
    else:
        l2.append(e)

# NOTE: misread problem, it says remove all duplicates like so:
# above example only removes two in a row...
# Example:
#?- compress([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
#X = [a,b,c,a,d,e]


# TODO: is there a simpler way with reduce:

# 1.19 (**) Rotate a list l n places to the left.
def rotate(l,n):
    return l[n:]+l[:n]
