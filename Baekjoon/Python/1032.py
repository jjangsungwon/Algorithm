if __name__ == "__main__":

    T = int(input())
    data = []
    result = []

    for i in range(T):
        temp = input()
        data.append(temp)

    if T == 1:
        print("".join(map(str, data[0])))
    else:
        for i in range(len(data[0])):
            temp = [data[0][i]]
            for j in range(1, T):
                if data[j][i] not in temp:
                    result.append("?")
                    break
                elif j == T - 1:
                    result.append(data[0][i])

        print("".join(map(str, result)))
