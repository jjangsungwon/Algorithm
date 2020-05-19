if __name__ == "__main__":

    T = int(input())

    for _ in range(T):
        pre_H, pre_M, pre_P, pre_D, post_H, post_M, post_P, post_D = map(int, input().split())

        # HP
        if pre_H + post_H <= 1:
            H = 1
        else:
            H = pre_H + post_H

        # MP
        if pre_M + post_M <= 1:
            M = 1
        else:
            M = pre_M + post_M

        # 공격력
        if pre_P + post_P <= 0:
            P = 0
        else:
            P = pre_P + post_P

        # 방어력
        D = pre_D + post_D

        result = 1 * H + 5 * M + 2 * P + 2 * D
        print(result)