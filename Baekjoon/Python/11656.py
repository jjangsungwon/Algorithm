import sys
import copy
from operator import itemgetter

if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    print('\n'.join(sorted([s[i:] for i in range(len(s))])))
    
    
    