import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = [0] * 10000

    for i in range(N):
        arr[int(sys.stdin.readline()) - 1] += 1

    for i in range(10000):
        for j in range(arr[i]):
            print(i+1)