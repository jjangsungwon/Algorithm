if __name__ == "__main__":
    N = int(input())  # 트로피의 개수
    data = [int(input()) for _ in range(N)]
    left_max, right_max = data[0], data[-1]  # 높이 초기값
    left_count, right_count = 1, 1  # 개수 초기값

    # 왼쪽 개수 파악
    for i in range(1, N):
        if left_max < data[i]:
            left_max = data[i]
            left_count += 1

    # 오른쪽 개수 파악
    for i in range(N - 2, -1, -1):
        if right_max < data[i]:
            right_max = data[i]
            right_count += 1

    # 출력
    print(left_count)
    print(right_count)