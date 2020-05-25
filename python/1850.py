import math


if __name__ == "__main__":

    A, B = map(int, input().split())

    GCD = math.gcd(A, B)
    result = [1] * GCD
    result = "".join(map(str, result))

    print(result)