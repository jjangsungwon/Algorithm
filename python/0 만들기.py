def dfs(idx, arr):  # 인덱스, 문자열 수식
    if idx == N - 1:
        eval_list = "".join(map(str, arr))
        result = eval(eval_list)
        if result == 0:
            for i in range(len(arr)):
                if arr[i] == "":
                    print(" ", end="")
                elif i == len(arr) - 1:
                    print(arr[i])
                else:
                    print(arr[i], end="")
    else:
        arr.insert(idx * 2 + 1, '')  # 숫자 이어 붙이기
        dfs(idx + 1, arr)
        arr.pop(idx * 2 + 1)

        arr.insert(idx * 2 + 1, '+')  # +
        dfs(idx + 1, arr)
        arr.pop(idx * 2 + 1)

        arr.insert(idx * 2 + 1, '-')  # -
        dfs(idx + 1, arr)
        arr.pop(idx * 2 + 1)


if __name__ == "__main__":

    testcase = int(input())  # 테스트 케이스의 개수
    for _ in range(testcase):
        N = int(input())  # 1 ~ N
        N_list = [i for i in range(1, N + 1)]
        dfs(0, N_list)
        print("")
