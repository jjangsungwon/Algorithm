if __name__ == "__main__":

    N = int(input())
    cost = list(map(int, input().split()))
    M = int(input())

    left, right = 1, max(cost)

    max_val = 0
    while left <= right:
        mid = (left + right) // 2
        total = 0
        for i in range(len(cost)):
            if cost[i] >= mid:
                total += mid
            else:
                total += cost[i]

        if max_val < total <= M:
            max_val = mid
            left = mid + 1
        else:
            right = mid - 1
    print(max_val)
