if __name__ == "__main__":

    T = int(input())

    for _ in range(T):
        N, K = map(int, input().split())
        candy = list(map(int, input().split()))
        total = 0
        for i in range(len(candy)):
            total += candy[i] // K
        print(total)