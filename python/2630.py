def solution(arr):
    result = []

    size = len(arr) // 2
    quadrant_1 = []
    for i in range(size):
        quadrant_1.append(arr[i][:size])

    quadrant_2 = []
    for i in range(size):
        quadrant_2.append(arr[i][size:])

    quadrant_3 = []
    for i in range(size, len(arr)):
        quadrant_3.append(arr[i][:size])

    quadrant_4 = []
    for i in range(size, len(arr)):
        quadrant_4.append(arr[i][size:])

    result.append(quadrant_1)
    result.append(quadrant_2)
    result.append(quadrant_3)
    result.append(quadrant_4)

    return result


if __name__ == "__main__":

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    white_cnt, blue_cnt = 0, 0
    queue = [arr]

    # 4부분으로 나누기
    arr = queue.pop(0)
    arr = solution(arr)

    while True:

        for k in range(len(arr)):
            s = 0
            for i in range(len(arr[k])):
                s += sum(arr[k][i])
            if s == len(arr[k]) * len(arr[k]):
                blue_cnt += 1
            elif s == 0:
                white_cnt += 1
            else:
                result = solution(arr[k])
                for i in range(len(result)):
                    queue.append([result[i]])
        if len(queue) == 0:
            break
        arr = queue.pop(0)
    print(white_cnt)
    print(blue_cnt)
