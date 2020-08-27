if __name__ == "__main__":

    T = int(input())

    for i in range(T):
        n = int(input())

        if n == 0:
            print("1 0")
        elif n == 1:
            print("0 1")
        elif n == 2:
            print("1 1")
        elif n == 3:
            print("1 2")
        elif n == 4:
            print("2 3")
        else:
            dp_one = [0 for _ in range(3, n + 1)]
            dp_zero = [0 for _ in range(3, n + 1)]

            dp_one[0], dp_one[1] = 2, 3
            dp_zero[0], dp_zero[1] = 1, 2

            for i in range(2, len(dp_one)):
                dp_one[i] = dp_one[i-1] + dp_one[i-2]
                dp_zero[i] = dp_zero[i-1] + dp_zero[i-2]

            print(dp_zero[len(dp_zero) - 1], dp_one[len(dp_one) - 1])