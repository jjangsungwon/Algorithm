if __name__ == "__main__":

    A, B = map(int, input().split())
    answer = 0
    # -3 -2 -1
    if A < 0 and B < 0:
        answer = ((min(A, B) * (min(A, B) - 1)) // 2 - (max(A, B) + 1) * max(A, B) // 2) * -1
    elif A < 0 and B >= 0:
        answer = (A * (A - 1) // 2) * -1 + B * (B + 1) // 2
    elif A >= 0 and B < 0:
        answer = (A * (A + 1) // 2) + (B * (B - 1) // 2) * -1
    elif A >= 0 and B >= 0:
        answer = (max(A, B) * (max(A, B) + 1)) // 2 - ((min(A, B) - 1) * min(A, B) // 2)

    print(answer)
