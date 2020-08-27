import sys

if __name__ == "__main__":

    N = int(sys.stdin.readline())

    for i in range(N - 1):
        print(" " * i, end="")
        print("*" * (2 * N - (1 + i * 2)))


    for i in range(N-1, -1, -1):
        print(" " * i, end="")
        print("*" * ((2 * N - 1) - (i * 2)))



