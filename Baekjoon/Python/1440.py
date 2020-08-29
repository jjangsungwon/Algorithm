if __name__ == "__main__":
    time = input()

    # 시간, 분, 초 리스트 초기화
    h, m, s = [], [], []

    # time에 있는 숫자 3개 뽑기
    a = int(time[:2])
    b = int(time[3:5])
    c = int(time[6:])
    num = [a, b, c]

    # h, m, s에 들어갈 수 있는 수 확인
    for value in num:
        if 1 <= value <= 12:
            h.append(value)
        if 0 <= value <= 59:
            m.append(value)
            s.append(value)

    # 경우의 수 계산
    answer = len(h) * (len(m) - 1) * (len(s) - 2)
    print(answer)
