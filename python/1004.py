import math


if __name__ == "__main__":

    T = int(input())

    for _ in range(T):
        x1, y1, x2, y2 = map(int, input().split())  # 출발점, 도착점

        n = int(input())
        circle = []
        cnt = 0
        for _ in range(n):
            x3, y3, r = map(int, input().split())

            if pow(x3 - x1, 2) + pow(y3 - y1, 2) >= r * r or pow(x3 - x2, 2) + pow(y3 - y2, 2) >= r * r:
                if pow(x3 - x1, 2) + pow(y3 - y1, 2) <= r * r:
                    cnt += 1
                if pow(x3 - x2, 2) + pow(y3 - y2, 2) <= r * r:
                    cnt += 1

        print(cnt)