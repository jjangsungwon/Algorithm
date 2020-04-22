def pre_permutation(arr):
    length = len(arr) - 1
    i = length
    j = length

    while arr[i-1] < arr[i]:
        i -= 1

    if i == 0:
        return -1

    while arr[i-1] < arr[j]:
        j -= 1

    arr[i-1], arr[j] = arr[j], arr[i-1]

    j = length

    while i < j and arr[i] < arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return arr


if __name__ == "__main__":

    N = int(input())
    data = list(map(int, input().split()))

    result = pre_permutation(data)

    if result == -1:
        print(result)
    else:
        print(" ".join(map(str, data)))