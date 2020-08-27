if __name__ == "__main__":

    while True:
        num = input()

        if num == "#":
            break

        result, val = 0, 1
        operation = ["-", "\\", "(", "@", "?", ">", "&", "%"]
        for i in range(len(num) -1, -1, -1):
            if num[i] not in operation:
                result += val * -1
            else:
                result += val * operation.index(num[i])
            val *= 8

        print(result)
