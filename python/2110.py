import itertools


if __name__ == "__main__":

    N, C = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    # 1 2 4 8 9
    arr.sort()
    left, right = 1, max(arr) - min(arr)

    max_length = -1
    while left <= right:
        mid = (left + right) // 2
        index, cnt = 0, 1
        for i in range(1, len(arr)):
            if arr[i] - arr[index] >= mid:
                cnt += 1
                index = i

        if cnt >= C:
            left = mid + 1
            max_length = max(max_length, mid)
        else:
            right = mid - 1
    print(max_length)
