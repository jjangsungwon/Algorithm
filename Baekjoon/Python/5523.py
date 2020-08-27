if __name__ == "__main__":

    N = int(input())
    cnt_A, cnt_B = 0, 0
    for _ in range(N):
        A, B = map(int, input().split())

        # 비긴 경우
        if A == B:
            continue
        # A가 이긴 경우
        elif A > B:
            cnt_A += 1
        else:
            cnt_B += 1

    print(cnt_A, cnt_B)
