if __name__ == "__main__":

    line = [input() for _ in range(5)]
    length = 0
    for i in range(len(line)):
        length = max(length, len(line[i]))

    result = ""

    for j in range(length):
        for i in range(5):
            if len(line[i]) <= j:
                continue
            else:
                result += line[i][j]
    print(result)
