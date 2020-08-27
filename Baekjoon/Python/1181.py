if __name__ == "__main__":

    T = int(input())
    data = []
    result = []

    for i in range(T):
        temp = input()

        if temp in data:
            continue
        else:
            data.append(temp)

    for i in range(len(data)):
        result.append((len(data[i]), data[i]))

    result = sorted(result, key=lambda x: (x[0], x[1]))

    for i in range(len(result)):
        print(result[i][1])
