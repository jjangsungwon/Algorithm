import sys

INF = 1e9
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


if __name__ == "__main__":
    n, m, t, d = map(int, sys.stdin.readline().split())
    array = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]  # 산의 지도 입력받음

    # 산의 지도를 숫자 형태로 변환
    for i in range(n):
        for j in range(m):
            if "A" <= array[i][j] <= "Z":  # 대문자
                array[i][j] = ord(array[i][j]) - 65
            else:
                array[i][j] = ord(array[i][j]) - 71

    # 거리 배열 초기화
    distance = [[INF] * 626 for _ in range(626)]  # n, m 최댓값 25
    for i in range(626):
        distance[i][i] = 0  # 자기 자신은 0

    # 거리 계산
    for x in range(n):
        for y in range(m):
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    dif = array[x][y] - array[nx][ny]  # 높이 차이 계산
                    if abs(dif) > t:  # t보다 높이 차이가 크면 이동 불가
                        continue
                    if 0 <= dif:  # 높이가 낮은 곳이나 같은 곳으로 이동
                        distance[x * m + y][nx * m + ny] = 1  # 원래 위치에서 해당 위치까지의 거리
                    else:
                        distance[x * m + y][nx * m + ny] = dif * dif  # 높이 차 제곱

    # 플로이드 워셜
    for k in range(n * m):
        for i in range(n * m):
            for j in range(n * m):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    # 높이 찾기
    height = 0
    for i in range(n):
        for j in range(m):
            if distance[0][i * m + j] + distance[i * m + j][0] <= d:
                height = max(height, array[i][j])
    print(height)