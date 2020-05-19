if __name__ == "__main__":

    N = int(input())
    people = list(map(int, input().split()))

    cnt = 0
    for i in range(1, N + 1):
        if people[i - 1] != i:
            cnt += 1
    print(cnt)
