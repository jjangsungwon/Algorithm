import sys

if __name__ == "__main__":
    N = int(input())
    data = [int(input()) for _ in range(N)]

    # 정렬
    data.sort()

    # 불만도 합 계산
    answer = 0
    for i in range(N):
        answer += abs(i + 1 - data[i])

    print(answer)
