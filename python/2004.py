def n_count(n, div):
    answer = 0
    while n != 0:
        n //= div
        answer += n
    return answer


if __name__ == "__main__":

    n, m = map(int, input().split())

    if m == 0:
        print(0)
    else:
        two = n_count(n, 2) - n_count(m, 2) - n_count(n - m, 2)
        five = n_count(n, 5) - n_count(m, 5) - n_count(n - m, 5)

        if two < five:
            print(two)
        else:
            print(five)
