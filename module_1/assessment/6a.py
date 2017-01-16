# clean up
# what would happen if you used deepcopy instead of copy?
In [6]: def is_immutable(val):
   ...:     """ if mem address doesn't change then immutable """
   ...:     return id(val) == id(copy.copy(val))
   ...:

In [7]: is_immutable(5)
Out[7]: True

In [8]: is_immutable('hi')
Out[8]: True

In [9]: is_immutable((1,2))
Out[9]: True

In [10]: is_immutable([1,2])
Out[10]: False
