from operator import itemgetter

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N = int(input())
        arr = []
        cnt = 0

        for i in range(N):
            temp = list(map(int, input().split()))
            arr.append(temp)

        arr.sort(key=itemgetter(1))

        end = arr[0][1]
        cnt += 1

        for i in range(1, N):
            if arr[i][0] < end:
                continue
            else:
                cnt += 1
                end = arr[i][1]

        print("#{0} {1}".format(tc, cnt))


