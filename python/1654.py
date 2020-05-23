if __name__ == "__main__":

    # input
    K, N = map(int, input().split())
    line = [int(input()) for _ in range(K)]

    left, right = 1, max(line)

    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for i in range(len(line)):
            cnt += line[i] // mid

        if cnt >= N:
            left = mid + 1
        else:
            right = mid - 1
    print(right)
