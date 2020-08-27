import math


if __name__ == "__main__":

    A1, B1 = map(int, input().split())
    A2, B2 = map(int, input().split())

    LCM = B1 * B2 // math.gcd(B1, B2)
    A1 *= LCM // B1
    A2 *= LCM // B2

    A = A1 + A2
    B = LCM

    gcd = 0
    while gcd != 1:
        gcd = math.gcd(A, B)
        A //= gcd
        B //= gcd

    print(A, B)
