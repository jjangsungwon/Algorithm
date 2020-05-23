if __name__ == "__main__":

    N, K = map(int, input().split())
    arr = [1] * N

    cnt, index = 0, 0
    print("<", end="")
    while sum(arr) != 0:
        if arr[index]:
            cnt += 1

        if cnt == K:
            if sum(arr) == 1:
                print(index + 1, end="")
            else:
                print(index + 1, end=", ")
            arr[index] = 0
            cnt = 0
        index += 1
        if index >= len(arr):
            index = 0
    print(">")

