from collections import deque
import sys

sys.setrecursionlimit(10 ** 9)


def dfs(start_col):
    global array, location

    row, col = location[start_col][-1]
    while array[row][col] == 'O':  # 이미 갱신이 되었던 곳이라면 이전에 들렸던 곳으로 되돌아간다.
        row, col = location[start_col].pop()

    while True:
        location[start_col].append([row, col])  # 위치 리스트에 추가한다.

        if row == r - 1:  # 가장 아랫줄이라면 종료한다.
            break
        elif array[row + 1][col] == 'X':  # 아랫칸이 벽으로 막혀있으면 종료한다.
            break
        elif array[row + 1][col] == '.':  # 아랫칸이 빈공간이면 이동한다.
            row += 1
        else:  # 아랫칸에 돌이 있는 경우
            if col - 1 >= 0 and row + 1 < r and array[row][col - 1] == '.' and array[row + 1][col - 1] == '.':  # 왼쪽, 왼쪽 아래 칸이 비어있다면 왼쪽으로 미끄러진다.
                row += 1
                col -= 1
            elif col + 1 < c and row + 1 < r and array[row][col + 1] == '.' and array[row + 1][col + 1] == '.':  # 왼쪽 못가고 오른쪽, 오른쪽 아래 비어있다면
                row += 1
                col += 1
            else:  # 종료한다
                break
    array[row][col] = 'O'  # 돌을 놓는다.


if __name__ == "__main__":
    r, c = map(int, sys.stdin.readline().split())  # 보드의 크기 입력받음
    array = [list(sys.stdin.readline().strip()) for _ in range(r)]
    n = int(sys.stdin.readline().strip())  # 돌의 개수 입력받음
    data = [int(sys.stdin.readline().strip()) for _ in range(n)]  # 돌을 덜진 열의 위치 입력받음
    location = deque(deque() for _ in range(c + 1))

    for i in range(n):  # 돌의 개수 입력받음
        location[data[i] - 1].append([0, data[i] - 1])  # 돌을 놓는 위치를 최대한 빨리 찾기 위해서 이전 위치들을 저장한다.
    for i in range(n):  # 돌의 개수만큼 반복
        dfs(data[i] - 1)

    # 최종 상태 출력
    for i in range(r):
        print("".join(map(str, array[i])))
