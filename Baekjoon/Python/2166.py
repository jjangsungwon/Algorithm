"""
    2차원 평면상에 여러개의 점으로 이루어진 다각형의 면적을 구하는 프로그램 작성
    신발끈의 공식 사용
    (x1*y2 + ... + xn-1*yn + xny1 - (x2y1 + x3y2 ... + xnyn-1 + x1yn)) * 1/2
"""

if __name__ == "__main__":
    n = int(input())  # 점의 개수
    data = [list(map(int, input().split())) for _ in range(n)]

    answer = 0
    for i in range(n - 1):
        answer += data[i][0] * data[i + 1][1]
    answer += data[n - 1][0] * data[0][1]

    for i in range(1, n):
        answer -= data[i][0] * data[i - 1][1]
    answer -= data[0][0] * data[n - 1][1]

    answer = answer / 2
    print(abs(answer))