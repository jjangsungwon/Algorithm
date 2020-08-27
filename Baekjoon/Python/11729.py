def hanoi(n, start, middle, end):
    if n == 1:  # 종료 조건
        move.append((start, end))
    else:
        hanoi(n - 1, start, end, middle)  # 1번 기둥에 있는 원반 중 n-1개를 2번 기둥으로 옮김(3번 기둥 이용)
        move.append((start, end))  # 1번 기둥에 남아 있는 가장 큰 원반을 3번 기둥으로 옮김
        hanoi(n - 1, middle, start, end)  # 1번 기둥에 있는 원반 중 n-1개를 2번 기둥으로 옮김(3번 기둥 이용)


if __name__ == "__main__":
    N = int(input())

    move = []
    hanoi(N, 1, 2, 3)
    print(len(move))

    for i, j in move:
        print(i, j)
