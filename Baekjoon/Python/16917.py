if __name__ == "__main__":

    # input
    A, B, C, X, Y = map(int, input().split())
    money = 0

    # 반반 < 후라이드 + 양념
    if 2 * C < A + B:
        money += min(X, Y) * 2 * C
        X, Y = X - min(X, Y), Y - min(X, Y)

        if X == 0:  # 후라이드 치킨이 남았을때
            money += min(B, 2 * C) * Y
        elif Y == 0:  # 양념 치킨이 남았을때
            money += min(A, 2 * C) * X
    else:
        money += A * X + B * Y

    print(money)