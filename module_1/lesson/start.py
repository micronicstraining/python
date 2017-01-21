# Index of lessons

# Recommended reading order:

# 0) explore_REPL

# 1) none.py
a = None

# 2) bool.py
b = True or False and not True or (True and not False)

# 3) integers.py
c = ((2**8) - 1) | (0b0101010101) + 0xff

# 4) float.py
d = 3.1415

# 5) numbers.py (skip)
e = complex(-1, 0)

# 6) string.py
f = """Let's explore strings!"""

# 7) flow control 1

# 8) tuple.py
g, h, *i = (1,2,3,4,5,6,7,8,9,10)
g2, h2, i2, *_ = (1, 'hi', 3.14, None, None, None, None)

# 9) namedtuple.py (skip)
from collections import namedtuple
IPAddress = namedtuple("IPAddress", 'o1 o2 o3 o4')
ip = IPAddress(o1=192, o2=168, o3=100, o4=1)

# 10) matrixtuple.py (skip)
i_, j_, k_ = ((1,2,3), (4,5,6), (7,8,9))

# 11) list.py (sort)

# 12) flow control 2

# 13) functions 1

# 14) array.py (skip)

# 15) deque.py (skip)

# 16) set.py

# 17) frozenset.py (skip)

# 18) dictionary.py

# 19) functions 2

# 20) flow control 3 (exceptions)

# 21) classes (3 types of scope)

# 22) modules

# 23) packages
