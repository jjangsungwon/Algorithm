if __name__ == "__main__":

    # input
    A, B = map(int, input().split())
    C, D = map(int, input().split())

    result = max(max(max(A/C + B/D, C/D + A/B), D/B + C/A), B/A + D/C)

    cnt = 0
    if result == C/D + A/B:
        cnt = 1
    elif result == D/B + C/A:
        cnt = 2
    elif result == B/A + D/C:
        cnt = 3

    print(cnt)
