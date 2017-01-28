a = dict(one=1, two=2, three=3)
      
b = {'one': 1, 'two': 2, 'three': 3}
     
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
      
d = dict([('two', 2), ('one', 1), ('three', 3)])

     
# should be true
assert(a == b == c == d)
