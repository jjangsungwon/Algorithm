if __name__ == "__main__":
    n, s = map(int, input().split())  # 수열의 길이, 목표 합
    data = list(map(int, input().split()))

    left, right = 0, 1

    total = data[0]
    answer = 1e9
    while left <= right < n:
        if total < s:
            total += data[right]
            right += 1
        else:
            answer = min(answer, right - left)
            total -= data[left]
            left += 1

    if right >= n:
        while left < right:
            if total >= s:
                total -= data[left]
                answer = min(answer, right - left)
                left += 1
            else:
                break

    if answer == 1e9:
        print(0)
    else:
        print(answer)