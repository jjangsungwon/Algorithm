if __name__ == "__main__":

    # input
    N = int(input())
    charge = list(map(int, input().split()))

    y, m = 0, 0
    for i in range(len(charge)):
        y += (charge[i] // 30 + 1) * 10
        m += (charge[i] // 60 + 1) * 15

    if y == m:
        print('Y M', y)
    elif y > m:
        print('M', m)
    else:
        print('Y', y)
