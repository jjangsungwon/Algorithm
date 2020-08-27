if __name__ == "__main__":

    N, M, K = map(int, input().split())

    row = K // M
    col = K % M

    print(row, col)
