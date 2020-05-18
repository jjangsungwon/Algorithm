import math

if __name__ == "__main__":

    N, K = map(int, input().split())

    prime = [1] * (N + 1)
    cnt = 0
    for i in range(2, N + 1):
        for j in range(i, N + 1, i):
            if prime[j] == 1:
                cnt += 1
                prime[j] = 0

                if cnt == K:
                    print(j)
