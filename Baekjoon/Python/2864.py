if __name__ == "__main__":

    A, B = map(str, input().split())
    A, B = list(A), list(B)

    # 최댓값 (모든 5를 6으로 바꾼 경우)
    for i in range(len(A)):
        if A[i] == '5':
            A[i] = '6'
    for i in range(len(B)):
        if B[i] == '5':
            B[i] = '6'
    max_answer = int("".join(map(str, A))) + int("".join(map(str, B)))

    # 최솟값 (모든 6을 5로 바꾼 값)
    for i in range(len(A)):
        if A[i] == '6':
            A[i] = '5'
    for i in range(len(B)):
        if B[i] == '6':
            B[i] = '5'
    min_answer = int("".join(map(str, A))) + int("".join(map(str, B)))

    print(min_answer, max_answer)
