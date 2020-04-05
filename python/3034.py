import math

if __name__ == "__main__":

    N, W, H = map(int, input().split())

    limit = math.sqrt(pow(W, 2) + pow(H, 2))

    for _ in range(N):
        value = int(input())

        if limit >= value:
            print("DA")
        else:
            print("NE")