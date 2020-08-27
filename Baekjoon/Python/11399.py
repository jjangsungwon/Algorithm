import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    accrue = [0 for _ in range(N)]

    # 정렬(오름차순)
    arr.sort()

    # 대기 시간
    accrue[0] = arr[0]
    for i in range(1, N):
        accrue[i] = accrue[i-1] + arr[i]

    print(sum(accrue))
