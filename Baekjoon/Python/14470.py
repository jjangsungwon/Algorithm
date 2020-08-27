if __name__ == "__main__":

    # input
    meat = []
    for _ in range(5):
        meat.append(int(input()))
    time = 0
    if meat[0] < 0:  # 고기가 얼어있는 상황
        time = abs(meat[0]) * meat[2] + meat[3] + meat[1] * meat[4]
    else:  # 고기가 얼어있지 않은 상황
        time = (meat[1] - meat[0]) * meat[4]

    print(time)