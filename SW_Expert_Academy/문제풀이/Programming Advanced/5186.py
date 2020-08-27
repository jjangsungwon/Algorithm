if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        n = float(input())
        arr = []

        while n > 0:
            n *= 2

            if n >= 1:
                arr.append(1)
                n -= 1
            else:
                arr.append(0)

            if len(arr) >= 13:
                break

        if len(arr) >= 13:
            print("#{0} overflow".format(tc))
        else:
            print("#{0} ".format(tc) + "".join(map(str, arr)))
