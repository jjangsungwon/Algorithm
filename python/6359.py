if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        n = int(input())

        # 1 - open, -1 - close
        room = [1] * (n + 1)

        for i in range(2, n + 1):
            for j in range(i, n + 1, i):
                room[j] *= -1
        # delete room 0
        room.pop(0)

        # print
        print(room.count(1))