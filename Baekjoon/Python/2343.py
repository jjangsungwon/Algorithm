if __name__ == "__main__":

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    lesson_total = sum(arr)
    left, right = lesson_total // M, sum(arr)
    # print(left, right)
    answer = right
    while left <= right:
        mid = (left + right) // 2

        if mid < max(arr):
            left = mid + 1
            continue
        # 조건 만족 확인
        count, temp = 0, 0
        for i in range(len(arr)):
            if arr[i] > mid:
                break
            elif temp + arr[i] <= mid:
                temp += arr[i]
            else:
                temp = arr[i]
                count += 1

        if count <= M - 1:  # 가능한 경우 (더 작은 값이 있는지 확인해야 한다)
            right = mid - 1
            answer = min(answer, mid)  # answer 값 업데이트
        else:  # 값을 증가시켜야 한다.
            left = mid + 1

    print(answer)
