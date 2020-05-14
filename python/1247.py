if __name__ == "__main__":

    # 3개의 테스트를 입력받는다
    for _ in range(3):
        N = int(input())
        num = []
        for i in range(N):
            num.append(int(input()))

        if sum(num) > 0:
            print("+")
        elif sum(num) == 0:
            print("0")
        else:
            print("-")

