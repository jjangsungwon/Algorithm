if __name__ == "__main__":

    M = int(input())

    ball = [0, 1, 0, 0]
    for i in range(M):
        X, Y = map(int, input().split())

        if X == Y:  # 같으면 의미 없다.
            continue
        else:
            ball[X], ball[Y] = ball[Y], ball[X]

    print(ball.index(1))
