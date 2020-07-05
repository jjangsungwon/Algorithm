# boj 11758

if __name__ == "__main__":

    # input
    p1 = list(map(int, input().split()))
    p2 = list(map(int, input().split()))
    p3 = list(map(int, input().split()))

    # x1 * y2 + x2 * y3 + x3 * y1 - (y1 * x2 + y2 * x3 + y3 * x1)
    answer = (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]) - (p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0])

    if answer == 0:
        print(0)
    elif answer > 0:
        print(1)
    else:
        print(-1)
