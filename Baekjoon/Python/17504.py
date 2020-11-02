from math import gcd


def dfs(idx, array, temp_p, temp_q):
    if idx == n:
        temp_p = temp_q - temp_p
        return temp_p, temp_q

    if idx == 0:
        temp_p = 1
        temp_q = array[idx]
    else:
        temp_p = array[idx] * temp_q + temp_p
        temp_p, temp_q = temp_q, temp_p
    return dfs(idx + 1, array, temp_p, temp_q)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()

    p, q = dfs(0, a, 0, 0)

    while True:
        max_divisor = gcd(p, q)
        if max_divisor == 1:
            break
        else:
            p %= max_divisor
            q %= max_divisor

    print(p, q)