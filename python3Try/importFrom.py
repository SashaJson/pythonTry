#  https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%B0%D1%8F_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B0_Python

import math
import time
import os
import random as r
from module import hi as h, add

try:
    import nomodule
except ImportError:
    print('Module "nomodule not exist"')

print(math.e)
print(time.time())
print(os.getcwdb())
print(os.uname())
print(r.random())

h()

print(add(25, 25))