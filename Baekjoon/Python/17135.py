from itertools import combinations
import copy


def check(array):
    for i in range(n):
        for j in range(m):
            if array[i][j] == 1:
                return False
    return True


def solve(data, array, cnt):
    if check(array):
        return cnt

    # 각 궁수가 죽일 수 있는 위치 저장
    location = [[] for _ in range(3)]
    for i in range(n):
        for j in range(m):
            if array[i][j] == 1:
                for k in range(3):
                    if abs(n - i) + abs(j - data[k]) <= d:
                        location[k].append([i, j])

    # 각 궁수가 죽일 수 있는 위치 중 거리가 가장 가까운 적 제거(거리가 같다면 제일 왼쪽 값)
    for i in range(3):
        if len(location[i]) == 0:
            continue
        else:
            location[i].sort(key=lambda x:(abs(n - x[0]) + abs(data[i] - x[1]), x[1]))
            if array[location[i][0][0]][location[i][0][1]] == 1:
                array[location[i][0][0]][location[i][0][1]] = 0
                cnt += 1

    # 적 1칸씩 아래로 이동
    for i in range(n - 1, -1, -1):
        for j in range(m):
            if array[i][j] == 1:
                if i == n - 1:
                    array[i][j] = 0
                else:
                    array[i + 1][j] = array[i][j]
                    array[i][j] = 0
    return solve(data, array, cnt)


if __name__ == "__main__":
    n, m, d = map(int, input().split())  # 행, 열, 공격 거리 입력
    maps = [list(map(int, input().split())) for _ in range(n)]
    index = [i for i in range(m)]  # 성 인덱스

    answer = 0
    for data in combinations(index, 3):
        copy_maps = copy.deepcopy(maps)
        answer = max(answer, solve(data, copy_maps, 0))

    print(answer)