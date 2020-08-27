# 수 3개를 이용해서 연도를 나타낸다.
# 지구(E), 태양(S), 달(M)

if __name__ == "__main__":
    E, S, M = map(int, input().split())

    init_E, init_S, init_M = 1, 1, 1
    year = 1

    while E + S + M != 3:
        if E == 1:
            E = 15
        else:
            E -= 1

        if S == 1:
            S = 28
        else:
            S -= 1

        if M == 1:
            M = 19
        else:
            M -= 1

        year += 1

    print(year)