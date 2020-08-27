# boj 6064
# blog : jjangsungwon.tistory.com

import sys

if __name__ == "__main__":

    T = int(input())  # 테스트 개수

    for _ in range(T):
        M, N, x, y = map(int, sys.stdin.readline().split())

        flag = 1
        while x <= M * N and flag:
            if (x - y) % N == 0:
                print(x)
                flag = False
            x += M

        if flag:
            print(-1)



