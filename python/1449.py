if __name__ == "__main__":
    N, L = map(int, input().split())
    data = list(map(int, input().split()))

    # 위치 내림차순 정렬
    data.sort()

    # 제일 왼쪽부터 수리 시작
    answer = 0
    temp = []  # 수리 값 저장
    for i in range(len(data)):
        if len(temp) == 0:  # 비어있는 경우
            answer += 1
            temp.append(data[i])
        else:
            if data[i] - temp[0] <= L - 1:  # 수리 가능 여부 확인 (0.5 때문에 -1 추가)
                temp.append(data[i])
            else:
                temp.clear()  # 수리 완료
                temp.append(data[i])
                answer += 1

    # 출력
    print(answer)