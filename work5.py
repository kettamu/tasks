from itertools import *

__author__ = 'mityagov_vi'
print sorted('dhabaa32134')

for i in count(1):
    print i,
    if i >= 20:
        break
print
for i in takewhile(lambda x: x > 0, [1, -2, 3, -3]):
    print i
for i in dropwhile(lambda x: x > 0, [1, -2, 3, -3]):
    print i,
