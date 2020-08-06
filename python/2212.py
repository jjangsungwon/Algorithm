import sys


if __name__ == "__main__":
    N = int(input())
    K = int(input())

    # 센서의 위치 오름차순 정렬
    sensor = list(map(int, input().split()))
    sensor.sort()

    # 집중국의 개수가 n 이상
    if K >= N:
        print(0)
    else:
        # 각 센서 간의 거리를 계산하여 내림차순 정렬
        distances = []
        for i in range(1, N):
            value = sensor[i] - sensor[i - 1]
            distances.append(value)
        distances.sort(reverse=True)
        # print(distances)

        # 가장 긴 거리부터 하나씩 제거
        for i in range(K - 1):
            distances[i] = 0

        print(sum(distances))