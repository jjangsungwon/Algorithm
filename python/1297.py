import math


if __name__ == "__main__":

    T, H, W = map(int, input().split())

    a = T * T
    b = H * H
    c = W * W

    result = math.sqrt(a / (b + c))

    b = result * H
    c = result * W

    print(math.floor(b), math.floor(c))