if __name__ == "__main__":

    N = int(input())

    N = list(bin(N))
    if N.count('1') == 1:
        print(1)
    else:
        print(0)
