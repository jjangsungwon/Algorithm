import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for i in range(T):
        N, M = map(int, sys.stdin.readline().split())
        cnt = 0

        for n in range(N, M + 1):
            n = str(n)

            for i in range(len(n)):
                if n[i] == '0':
                    cnt +=1

        print(cnt)