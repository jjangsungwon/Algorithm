if __name__ == "__main__":

    N = int(input())
    name = [input() for _ in range(N)]
    first = {}

    # 개수 구하기
    for i in range(N):
        if name[i][0] in first.keys():
            first[name[i][0]] += 1
        else:
            first[name[i][0]] = 1

    result = []
    for index in first.keys():
        if first[index] >= 5:
            result.append(index)

    if len(result) == 0:
        print("PREDAJA")
    else:
        result.sort()
        print("".join(map(str, result)))