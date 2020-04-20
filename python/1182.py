import itertools


if __name__ == "__main__":

    # 5 0
    # -7 -3 -2 5 8

    N, S = map(int, input().split())
    data = list(map(int, input().split()))

    cnt = 0
    for i in range(1, N + 1):
        temp = list(itertools.combinations(data, i))

        for j in range(len(temp)):
            if sum(temp[j]) == S:
                cnt += 1

    print(cnt)

