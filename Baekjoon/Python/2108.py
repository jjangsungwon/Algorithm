import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    data = []
    mode = [0 for _ in range(8001)]

    for _ in range(N):
        temp = int(sys.stdin.readline())
        data.append(temp)
        mode[temp + 4000] += 1
    data.sort()

    # 산술평균
    average = sum(data) / N

    # 중앙값
    median = data[N // 2]

    # 최빈값

    value = max(mode)
    for _ in range(2):
        if max(mode) == value:
            mode_value = mode.index(max(mode)) - 4000
            mode[mode.index(max(mode))] = -4001


    # 범위
    range = max(data) - min(data)
    print("%.f" % average)
    print(median)
    print(mode_value)
    print(range)

    # -2 1 2 3 8