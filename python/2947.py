if __name__ == "__main__":

    # input
    order = list(map(int, input().split()))

    while order != sorted(order):
        if order[0] > order[1]:
            order[0], order[1] = order[1], order[0]
            print(" ".join(map(str, order)))

        if order[1] > order[2]:
            order[1], order[2] = order[2], order[1]
            print(" ".join(map(str, order)))

        if order[2] > order[3]:
            order[2], order[3] = order[3], order[2]
            print(" ".join(map(str, order)))

        if order[3] > order[4]:
            order[3], order[4] = order[4], order[3]
            print(" ".join(map(str, order)))