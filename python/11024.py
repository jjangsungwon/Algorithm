if __name__ == "__main__":

    T = int(input())

    for _ in range(T):
        num = list(map(int, input().split()))
        print(sum(num))