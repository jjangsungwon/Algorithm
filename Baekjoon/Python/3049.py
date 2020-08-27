if __name__ == "__main__":
    N = int(input())

    answer = N * (N - 1) * (N - 2) * (N - 3) // 24
    print(answer)
