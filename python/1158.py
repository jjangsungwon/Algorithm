# 1158_요세푸스 문제
if __name__ == "__main__":

    N, K = map(int, input().split())
    arr = [i for i in range(1, N + 1)]
    result = []

    index = K - 1
    while len(result) != N:
        if index >= len(arr):
            index %= len(arr)

        result.append(arr[index])
        arr.pop(index)
        index += K - 1

    print("<", end="")
    for i in range(len(result)):
        if i != len(result) - 1:
            print(str(result[i]) + ",", end=" ")
        else:
            print(result[i], end="")

    print(">")
