if __name__ == "__main__":

    while True:
        N = input()
        if N == '0':
            break

        while len(N) != 1:
            sub = 0
            for i in range(len(N)):
                sub += int(N[i])
            N = str(sub)
        print(N)