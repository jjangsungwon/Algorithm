import math


if __name__ == "__main__":

    N = int(input())

    point = 4

    for i in range(N):
        point = pow(math.sqrt(point) * 2 - 1, 2)

    print(int(point))