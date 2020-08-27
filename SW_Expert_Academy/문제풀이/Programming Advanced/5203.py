if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        card = list(map(int, input().split()))
        player_1 = []
        player_2 = []

        for i in range(len(card)):
            if i % 2 == 0:
                player_1.append(card[i])
            else:
                player_2.append(card[i])

        p1_check = 0
        p2_check = 0
        for n in range(4):
            p1_count = [0 for _ in range(10)]
            p2_count = [0 for _ in range(10)]

            p_1 = player_1[:n + 3]
            p_2 = player_2[:n + 3]

            for i in range(0, len(p_1)):
                p1_count[p_1[i]] += 1
                p2_count[p_2[i]] += 1

            # user1
            # triplet 검사
            for i in range(0, 10):
                if p1_count[i] >= 3:
                    p1_check = 1
                    break

            # run 검사
            cnt = 0
            if p1_check == 0:
                for i in range(0, 8):
                    if p1_count[i] >= 1 and p1_count[i+1] >= 1 and p1_count[i+2] >= 1:
                        p1_check = 1

            # user2
            # triplet 검사
            for i in range(0, 10):
                if p2_count[i] >= 3:
                    p2_check = 1
                    break

            # run 검사
            cnt = 0
            if p2_check == 0:
                for i in range(0, 8):
                    if p2_count[i] >= 1 and p2_count[i+1] >= 1 and p2_count[i+2] >= 1:
                        p2_check = 1

            if p1_check == 1:
                print("#{0} 1".format(tc))
                break
            elif p2_check == 1:
                print("#{0} 2".format(tc))
                break
            elif n == 3:
                print("#{0} 0".format(tc))
