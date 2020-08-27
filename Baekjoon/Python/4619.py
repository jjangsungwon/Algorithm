import sys


if __name__ == "__main__":

    while True:
        B, N = map(int, input().split())
        if B + N == 0:
            break

        val = -1
        dif = sys.maxsize
        for i in range(1, B + 1):
            if abs(pow(i, N) - B) <= dif:
                dif = abs(pow(i, N) - B)
                val = i
            else:
                break

        print(val)
