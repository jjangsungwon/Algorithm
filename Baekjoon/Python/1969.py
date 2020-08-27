if __name__ == "__main__":

    N, M = map(int, input().split())
    DNA = [input() for _ in range(N)]

    result = ""
    count = 0

    for i in range(M):
        temp = {}
        for j in range(N):
            if DNA[j][i] in temp.keys():
                temp[DNA[j][i]] += 1
            else:
                temp[DNA[j][i]] = 1

        max_val = 1
        max_string = ""
        sort_key = list(temp.keys())
        sort_key.sort()
        for index in sort_key:
            if temp[index] > max_val:
                max_val = temp[index]
                max_string = index

        if max_string == "":
            temp = []
            for j in range(N):
                temp.append(DNA[j][i])
            temp.sort()
            result += temp[0]
            count += N - 1
        else:
            count += N - temp[max_string]
            result += max_string

    print(result)
    print(count)

