if __name__ == "__main__":

    s, d = map(int, input().split())

    if s == 0 and d == 0:
        print(0, 0)
    elif (s + d) % 2 != 0 or s <= d:
        print(-1)
    else:
        a = (s + d) // 2
        b = s - a

        print(a, b)