def power(a, b):
    if b == 1:
        return a % C
    elif b == 2:
        return a * a % C
    else:
        temp = power(a, b // 2)
        if b % 2 == 0:
            return temp * temp % C
        else:
            return temp * temp * a % C


if __name__ == "__main__":
    A, B, C = map(int, input().split())

    result = power(A, B)
    print(result)