def solution(price, money, count):
    # count 만큼 놀이공원 이용
    sum = 0
    for i in range(1, count + 1):
        sum += price * i

    if sum <= money:  # 금액이 부족하지 않은 경우
        answer = 0
    else:  # 금액이 부족한 경우
        answer = sum - money

    return answer


if __name__ == "__main__":
    print(solution(3, 20, 4))
