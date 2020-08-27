if __name__ == "__main__":
    N, T = map(int, input().split())
    num = list(map(int, input().split()))

    cnt, total = 0, 0
    for i in range(len(num)):
        total += num[i]

        if total > T:
            break
        cnt += 1
    print(cnt)