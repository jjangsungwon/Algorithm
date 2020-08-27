if __name__ == "__main__":

    shuffle = input()

    # 초기 위치 1
    ball = 1

    for i in range(len(shuffle)):
        if shuffle[i] == 'A':
            if ball == 1:
                ball = 2
            elif ball == 2:
                ball = 1
        elif shuffle[i] == 'B':
            if ball == 2:
                ball = 3
            elif ball == 3:
                ball = 2
        else:
            if ball == 1:
                ball = 3
            elif ball == 3:
                ball = 1

    print(ball)



