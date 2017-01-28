# Solutions to
# https://sites.google.com/site/prologsite/prolog-problems/1

# 1.01 (*) Find the last element of a list.
l = [1,'test',(1,2,3),5,3,True,False,None,object,0,15,12]
l[-1]


# 1.02 (*) Find the last but one element of a list.
l[-2]


# 1.03 (*) Find the K'th element of a list.
# Note: Create a function that does this and make it return None if out of bounds
def kth_elem(k, l):
    if k < len(l):
        return l[k]
    return None


# 1.04 (*) Find the number of elements of a list.



# 1.05 (*) Reverse a list.l


# 1.05a Copy a list


# 1.06 (*) Find out whether a list is a palindrome.


# SKIP
# 1.07 (**) Flatten a nested list structure. (skip until recursion overview, go over fib example)


# SKIP
# 1.08 (**) Eliminate consecutive duplicates of list elements. (skip)


# 1.19 (**) Rotate a list l n places to the left.
