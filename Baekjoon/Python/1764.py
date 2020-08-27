import sys


if __name__ == "__main__":

    N, M = map(int, input().split())
    no_listen = set()
    no_see = set()

    for i in range(N):
        no_listen.add(sys.stdin.readline().rstrip())
    for i in range(M):
        no_see.add(sys.stdin.readline().rstrip())

    result = list(no_listen & no_see)
    result.sort()

    print(len(result))
    for i in range(len(result)):
        print(result[i])
