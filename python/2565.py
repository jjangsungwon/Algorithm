if __name__ == "__main__":

    wire = []
    # input
    N = int(input())
    for i in range(N):
        A, B = map(int, input().split())
        wire.append((A, B))

    wire = sorted(wire, key=lambda x: x[0])
    dp = [1] * N

    for i in range(N):
        for j in range(i):
            if wire[i][1] > wire[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(N - max(dp))
