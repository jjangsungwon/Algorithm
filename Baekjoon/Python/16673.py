if __name__ == "__main__":

    C, K, P = map(int, input().split())
    total = 0
    for i in range(1, C + 1):
        total += K * i + P * i * i
    print(total)