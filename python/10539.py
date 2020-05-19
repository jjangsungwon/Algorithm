if __name__ == "__main__":

    N = int(input())
    num = list(map(int, input().split()))
    A = [0] * len(num)

    A[0] = num[0]
    for i in range(1, len(num)):
        A[i] = num[i] * (i + 1) - sum(A[:i])

    print(" ".join(map(str, A)))
