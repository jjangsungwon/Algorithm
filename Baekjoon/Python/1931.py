import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = []
    result = []

    # 입력
    for i in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))

    arr = sorted(arr, key=lambda time: time[1])

    limit = 0
    count = 0

    for meeting in arr:
        if meeting[0] < limit:
            continue
        else:
            limit = meeting[1]
            count += 1

    print(count)
