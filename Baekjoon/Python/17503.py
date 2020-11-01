import sys

if __name__ == "__main__":
    n, m, k = map(int, sys.stdin.readline().split())
    data = []  # 맥주
    left, right = 1e9, 0
    for _ in range(k):
        temp = list(map(int, sys.stdin.readline().split()))
        data.append(temp)
        left = min(left, temp[1])
        right = max(right, temp[1])

    data.sort(reverse=True)  # 선호도를 기준으로 내림차순 정렬

    answer = 1e10
    while left <= right:
        mid = (left + right) // 2
        total = 0
        cnt = 0
        # 맥주 선호도 계산
        for i in range(k):
            if data[i][1] > mid:
                pass
            else:
                total += data[i][0]
                cnt += 1
                if cnt == n:
                    break
        if total >= m and cnt >= n:
            right = mid
            answer = min(answer, mid)
            if left == right:
                break
        else:
            left = mid + 1
    if answer != 1e10:
        print(answer)
    else:
        print(-1)

