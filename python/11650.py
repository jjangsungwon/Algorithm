import sys
from operator import itemgetter

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    data = []

    # input
    for i in range(N):
        x, y = map(int, sys.stdin.readline().split())
        data.append((x, y))

    # sort
    data.sort(key=itemgetter(0, 1))

    for i in data:
        print(" ".join(map(str, i)))