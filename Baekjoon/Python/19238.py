import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(row, col):
    global p, people

    # 현재 위치에서 가장 가까운 승객을 찾는다.
    if array[row][col] == 2:  # 같은 자리에 있는 경우
        candidate = [[row, col, people[(row, col)][0], people[(row, col)][1]]]
        distance = 0
    else:
        distance = sys.maxsize
        candidate = []  # 승객 후보
        q = deque()
        q.append([row, col, 0])
        visited = set()
        visited.add((row, col))
        while q:
            x, y, d = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if array[nx][ny] == 0 and (nx, ny) not in visited:
                        if p >= d + 1:  # 이동할 수 있는 거리
                            q.append([nx, ny, d + 1])
                            visited.add((nx, ny))
                    elif array[nx][ny] == 2 and (nx, ny) not in visited:  # 승객이 있다면
                        if p >= d + 1 and d + 1 <= distance:
                            distance = min(distance, d + 1)
                            candidate.append([nx, ny, people[(nx, ny)][0], people[(nx, ny)][1]])  # 후보 승객 추가
                            visited.add((nx, ny))

    if len(candidate) == 0:  # 태울 수 있는 승객이 없거나 다음 목적지로 이동할 수 없는 경우
        print(-1)
        sys.exit(0)
    else:
        # 후보 승객을 행 번호와 열 번호가 작은 순으로 정렬
        if len(candidate) != 1:
            candidate = sorted(candidate, key=lambda k: (k[0], k[1]))

        array[candidate[0][0]][candidate[0][1]] = 0  # 승객 탑승(2 -> 0)
        del people[(candidate[0][0], candidate[0][1])]
        p -= distance  # 이동 거리만큼 연료 감소
        if p < 0:  # 이동할 수 없는 경우
            print(-1)
            sys.exit(0)
        visited = set()
        visited.add((candidate[0][0], candidate[0][1]))
        # 승객을 목적지에 데려다 준다.
        start_row, start_col, final_row, final_col = candidate[0]
        q = deque()
        q.append([start_row, start_col, 0])
        while q:
            x, y, d = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if [nx, ny] == [final_row, final_col]:
                        p = p - (d + 1)  # 이동 완료
                        if p < 0:  # 연료가 부족한 상황
                            print(-1)
                            sys.exit(0)
                        else:  # 이동한만큼 연료 충전
                            p = p + (d + 1) * 2
                        return nx, ny
                    elif array[nx][ny] != 1 and (nx, ny) not in visited:
                        if p >= d + 1:
                            visited.add((nx, ny))
                            q.append([nx, ny, d + 1])
        print(-1)
        sys.exit(0)

if __name__ == "__main__":
    n, m, p = map(int, input().split())  # 지도 크기, 승객 수, 초기 연료량 입력받기
    array = [list(map(int, input().split())) for _ in range(n)]
    row, col = map(int, input().split())  # 시작 위치 입력받기
    people = {}
    for _ in range(m):  # 승객 정보 입력받기
        r, c, f_r, f_c = map(int, input().split())
        people[(r - 1, c - 1)] = (f_r - 1, f_c - 1)

    # 시작 지점 좌표 1씩 감소(인덱스 0부터 시작)
    row -= 1
    col -= 1

    # 지도에 승객 정보를 삽입한다.
    for key in people.keys():
        array[key[0]][key[1]] = 2

    for _ in range(m):  # 승객의 수만큼 반복
        row, col = bfs(row, col)

    # 남은 연료의 양 출력
    print(p)
