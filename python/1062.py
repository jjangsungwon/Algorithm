# check - 현재까지 배운 알파벳 인덱스 관련, count - 현재까지 배운 알파벳 개수
def backtracking(check, count):
    global max_cnt, visited, n, k, data

    if count == 0:  # 최대한 배웠을 때
        value = 0

        for i in range(n):
            flag = True
            word = data[i][4:-4]
            for j in range(len(word)):
                if not visited[ord(word[j]) - ord('a')]:
                    flag = False  # 만들 수 없는 수
                    break
            if flag:
                value += 1
            if value + n - i <= max_cnt:
                break
        max_cnt = max(max_cnt, value)

    else:
        for i in range(check, 26):
            if not visited[i]:
                visited[i] = True
                backtracking(i, count - 1)

                visited[i] = False


if __name__ == '__main__':
    n, k = list(map(int, input().rstrip().split()))
    data = [input() for _ in range(n)]

    max_cnt = 0
    visited = [False for _ in range(26)]
    must_alpha = [97, 99, 105, 110, 116]
    for i in range(len(must_alpha)):
        visited[must_alpha[i] - 97] = True

    if k < 5:
        print(0)
    else:
        backtracking(0, k - 5)
        print(max_cnt)
