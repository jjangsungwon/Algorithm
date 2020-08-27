import sys
sys.setrecursionlimit(10 ** 6)


def dfs(row, col, N):
    global minus_cnt, zero_cnt, plus_cnt, paper
    type = paper[row][col]
    flag = False

    for i in range(row, row + N):
        if flag:
            break

        for j in range(col, col + N):
            if paper[i][j] != type:
                k = N // 3

                # 9개로 자르기
                dfs(row, col, k)
                dfs(row + k, col, k)
                dfs(row + 2*k, col, k)

                dfs(row, col + k, k)
                dfs(row, col + 2 * k, k)

                dfs(row + k, col + k, k)
                dfs(row + k, col + 2*k, k)

                dfs(row + 2 * k, col + k, k)
                dfs(row + 2*k, col + 2*k, k)

                flag = True
                break

    if not flag:
        if paper[row][col] == -1:
            minus_cnt += 1
        elif paper[row][col] == 0:
            zero_cnt += 1
        else:
            plus_cnt += 1


if __name__ == "__main__":
    N = int(input())
    paper = [list(map(int, input().split())) for _ in range(N)]

    minus_cnt, zero_cnt, plus_cnt = 0, 0, 0

    dfs(0, 0, N)
    print(minus_cnt)
    print(zero_cnt)
    print(plus_cnt)
