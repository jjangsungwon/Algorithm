def BubbleSort(a): 
    for i in range(len(a) - 1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

def CountingSort(A, B, k):
    # A - 입력 리스트 사용된 숫자
    # B - 정렬된 리스트
    # C - 카운트 리스트

    C = [0] * K

    for i in range(0, len(B)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
