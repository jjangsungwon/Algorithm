if __name__ == "__main__":

    N, T, C, P = map(int, input().split())

    flag = 1
    money = 0
    for i in range(1, N + 1, T):
        if flag:  # 심을 수 있는 날
            flag = 0
        else:  # 수확
            money += P * C

    print(money)
