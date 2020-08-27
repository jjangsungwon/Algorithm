import math

if __name__ == "__main__":

    T = int(input())

    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())

        # 두 원 사이의 거리 (sqrt를 하면 소수점 계산이라 오차가 발생할 수 있어서 제외)
        distance = pow(x1 - x2, 2) + pow(y1 - y2, 2)

        if distance == 0 and r1 == r2:
            print(-1)
        elif distance == 0 and r1 != r2:
            print(0)
        elif distance == pow(r1 + r2, 2):
            print(1)
        elif distance == pow(r1 - r2, 2):
            print(1)
        elif distance < pow(r1 - r2, 2):
            print(0)
        elif distance > pow(r1 + r2, 2):
            print(0)
        else:  # distance < pow(r1 + r2, 2):
            print(2)
