T = int(input())

real_min = 1000000


def backtracking(count, sum):
    global real_min

    if sum > real_min:
        return

    if count == row:
        if real_min > sum:
            real_min = sum
        return

    for i in range(row):
        if visited[i] == 0:
            visited[i] = 1
            backtracking(count + 1, sum + data[count][i])
            visited[i] = 0


if __name__ == "__main__":
    for tc in range(1, T + 1):
        row = int(input())
        data = []
        visited = [0] * row
        real_min = 1000000

        for i in range(row):
            temp = list(map(int, input().split()))
            data.append(temp)

        backtracking(0, 0)
        print("#{0} {1}".format(tc, real_min))
