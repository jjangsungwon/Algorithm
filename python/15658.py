import sys


def dfs(cnt, val):
    global max_val, min_val

    if cnt == N:
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        return

    for i in range(4):
        if operation[i] >= 1:
            operation[i] -= 1
            if i == 0:
                dfs(cnt + 1, val + num[cnt])
            elif i == 1:
                dfs(cnt + 1, val - num[cnt])
            elif i == 2:
                dfs(cnt + 1, val * num[cnt])
            else:
                if val < 0:
                    dfs(cnt + 1, -(-val // num[cnt]))
                else:
                    dfs(cnt + 1, val // num[cnt])
            operation[i] += 1


if __name__ == "__main__":

    N = int(input())
    num = list(map(int, input().split()))
    operation = list(map(int, input().split()))

    max_val, min_val = -sys.maxsize, sys.maxsize
    dfs(1, num[0])

    print(max_val)
    print(min_val)