def prime(N):
    result = [True] * (N + 1)

    for i in range(2, N + 1):
        if result[i]:
            for j in range(i + i, N + 1, i):
                result[j] = False

    return [i for i in range(2, N + 1) if result[i]]


if __name__ == "__main__":
    N = int(input())

    data = prime(N)
    left = right = cnt = s = 0

    while True:
        if s >= N:
            s -= data[left]
            left += 1
        else:
            if right == len(data):
                break
            s += data[right]
            right += 1

        if s == N:
            cnt += 1

    print(cnt)
