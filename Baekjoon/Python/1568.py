if __name__ == "__main__":
    N = int(input()) # 새의 수
    answer = 0  # 걸리는 시간
    count = 1

    while N != 0:
        answer += 1
        if N >= count:  # 새가 날아갈 수 있는 상황
            N -= count
            count += 1
        else:
            N -= 1
            count = 2
    print(answer)