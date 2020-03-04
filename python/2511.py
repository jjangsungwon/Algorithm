import sys

if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a_score = 0
    b_score = 0
    flag = 0

    for i in range(10):
        if A[i] > B[i]:
            a_score += 3
            flag = 0
        elif A[i] < B[i]:
            b_score += 3
            flag = 1
        else:
            a_score += 1
            b_score += 1

    print(a_score, b_score)

    if a_score > b_score:
        print('A')
    elif a_score < b_score:
        print('B')
    else:
        if a_score == 10:
            print('D')
        elif flag == 1:
            print('B')
        else:
            print('A')