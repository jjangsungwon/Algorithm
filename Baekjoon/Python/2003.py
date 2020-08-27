if __name__ == "__main__":

    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    l_index = r_index = cnt = 0

    while True:
        if sum(data[l_index: r_index + 1]) >= M:
            l_index += 1
        else:
            if r_index == N:
                break
            r_index += 1

        if sum(data[l_index: r_index + 1]) == M:
            cnt += 1

    print(cnt)
