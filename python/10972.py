def next_permutation(arr):
    length = len(arr) - 1
    i = length
    j = length

    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1

    if i == 0:
        return -1

    while i != j and arr[i - 1] > arr[j]:
        j -= 1

    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    j = length

    while i <= j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


if __name__ == "__main__":
    N = int(input())
    data = list(map(int, input().split()))

    result = next_permutation(data)

    if result == -1:
        print(result)
    else:
        print(" ".join(map(str, result)))