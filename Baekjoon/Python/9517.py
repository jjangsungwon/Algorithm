if __name__ == "__main__":

    K = int(input())
    N = int(input())
    total = 0
    for i in range(N):
        T, Z = map(str, input().split())
        total += int(T)

        if total >= 210:
            print(K)
            exit()
        if Z != 'N' and Z != 'P':
            K += 1
        if K == 9:
            K = 1
