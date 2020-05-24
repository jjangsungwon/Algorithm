if __name__ == "__main__":

    N, M = map(int, input().split())
    tree = list(map(int, input().split()))

    left, right = 1, max(tree)

    max_height = 0
    while left <= right:
        mid = (left + right) // 2
        total = 0
        for i in range(len(tree)):
            if tree[i] > mid:
                total += tree[i] - mid

        if total >= M:
            max_height = max(max_height, mid)

        if total < M:
            right = mid - 1
        else:
            left = mid + 1
    print(max_height)