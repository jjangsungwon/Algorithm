if __name__ == "__main__":
    N, K = map(int, input().split())
    num_list = list(map(int, input().split()))
    num_list.sort()

    print(num_list[K - 1])
