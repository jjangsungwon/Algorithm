if __name__ == "__main__":
    n, k = map(int, input().split())

    array = [None] * n

    left_value = 1
    right_value = n

    for i in range(n):
        if k >= n - 1 - i:
            array[i] = right_value
            right_value -= 1
            k -= (n - 1 - i)
        else:
            array[i] = left_value
            left_value += 1
    if k == 0 and 'None' not in array:
        print(" ".join(map(str, array)))
    else:
        print(-1)