import sys


if __name__ == "__main__":
    n, m = map(int, input().split())  # 도시의 개수, 버스 노선의 개수
    distance = [sys.maxsize] * (n + 1)
    distance[1] = 0  # 시작 지점은 거리 1
    graph = [list(map(int, input().split())) for _ in range(m)]

    flag = False  # 음의 가중치 확인
    for i in range(n):
        for a, b, c in graph:
            if distance[a] != sys.maxsize and distance[b] > distance[a] + c:
                distance[b] = distance[a] + c
                if i == n - 1:  # 마지막에 업데이트 되는 것은 음의 사이클이 존재한다는 의미
                    print(-1)
                    sys.exit(0)

    for result in distance[2:]:
        if result == sys.maxsize:
            print(-1)
        else:
            print(result)