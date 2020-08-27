if __name__ == "__main__":

    T = int(input())

    for _ in range(T):

        N = int(input())
        cnt_1, cnt_2 = 0, 0
        for i in range(N):
            p1, p2 = map(str, input().split())
            if p1 == p2:
                continue
            elif p1 == "R":
                if p2 == "P":
                    cnt_2 += 1
                elif p2 == "S":
                    cnt_1 += 1
            elif p1 == "P":
                if p2 == "R":
                    cnt_1 += 1
                elif p2 == "S":
                    cnt_2 += 1
            elif p1 == "S":
                if p2 == "R":
                    cnt_2 += 1
                elif p2 == "P":
                    cnt_1 += 1

        if cnt_1 == cnt_2:
            print("TIE")
        elif cnt_1 > cnt_2:
            print("Player 1")
        else:
            print("Player 2")


