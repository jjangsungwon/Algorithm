"""
github blog : jjangsungwon.github.io
baekjoon : 10988
"""

import sys
import copy

string = list(sys.stdin.readline())
copy_string = copy.deepcopy(string)
string.reverse()

# '\n'제거
copy_string.pop(len(copy_string)-1)
string.pop(0)

if string == copy_string:
    print(1)
else:
    print(0)

