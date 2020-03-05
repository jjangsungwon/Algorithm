import sys
from operator import itemgetter

if __name__ == "__main__":
    N = int(sys.stdin.readline())

    for i in range(N):
        c = int(sys.stdin.readline())
        people = []

        for i in range(c):
            temp = list(sys.stdin.readline().split())
            temp[0] = int(temp[0])
            people.append(temp)

        people.sort(key=itemgetter(0), reverse=True)

        print(people[0][1])