if __name__ == "__main__":

    N = int(input())

    if N <= 3:
        print(N * 2)
    else:
        result = 6
        val = 3
        cnt = 0

        for i in range(4, N + 1):
            result += val
            cnt += 1

            if cnt == 2:
                cnt = 0
                val += 1

        print(result)
