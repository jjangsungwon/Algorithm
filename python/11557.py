import sys
from operator import itemgetter

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for i in range(T):
        N = int(sys.stdin.readline())
        data = []

        for j in range(N):
            temp = list(map(str, sys.stdin.readline().split()))
            temp[1] = int(temp[1])
            data.append(temp)

        data.sort(key=itemgetter(1), reverse=True)
        print(data[0][0])
