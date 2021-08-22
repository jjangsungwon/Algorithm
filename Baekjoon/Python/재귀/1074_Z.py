import sys


def divide(size, start_row, start_col):
    global cnt
    if size == 2:
        if start_row == r and start_col == c:  # 왼쪽 위
            print(cnt)
            sys.exit(0)
        if start_row == r and start_col + 1 == c:  # 오른쪽 위
            print(cnt + 1)
            sys.exit(0)
        if start_row + 1 == r and start_col == c:  # 왼쪽 아래
            print(cnt + 2)
            sys.exit(0)
        if start_row + 1 == r and start_col + 1 == c:  # 오른쪽 아래
            print(cnt + 3)
            sys.exit(0)
        cnt += 4
    else:
        if r <= start_row + size // 2 and c <= start_col + size // 2:
            divide(size // 2, start_row, start_col)
        else:
            cnt += (size // 2) ** 2

        if r <= start_row + size // 2 and c <= start_col + size // 2 * 2:
            divide(size // 2, start_row, start_col + size // 2)
        else:
            cnt += (size // 2) ** 2

        if r <= start_row + size // 2 * 2 and c <= start_col + size // 2:
            divide(size // 2, start_row + size // 2, start_col)
        else:
            cnt += (size // 2) ** 2

        if r <= start_row + size // 2 * 2 and c <= start_col + size // 2 * 2:
            divide(size // 2, start_row + size // 2, start_col + size // 2)
        else:
            cnt += (size // 2) ** 2


if __name__ == "__main__":

    N, r, c = map(int, sys.stdin.readline().split())

    cnt = 0
    divide(2 ** N, 0, 0)
