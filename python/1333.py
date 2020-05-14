if __name__ == "__main__":

    N, L, D = map(int, input().split())

    bell = []

    for i in range(N):
        for j in range(L):
            bell.append(1)  # 노래 재생

        for j in range(5):
            bell.append(0)  # 조용한 구간

    index = 0
    while True:
        if index >= len(bell):
            break
        elif bell[index] == 1:
            index += D
        elif bell[index] == 0:
            break

    print(index)