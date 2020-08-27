if __name__ == "__main__":

    while True:

        N = input()

        if N == '0':
            break

        length = 2 + len(N) - 1
        for i in range(len(N)):
            if N[i] == '1':
                length += 2
            elif N[i] == '0':
                length += 4
            else:
                length += 3

        print(length)
