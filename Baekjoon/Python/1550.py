if __name__ == "__main__":

    hex = input()

    val = 1
    result = 0
    for i in range(len(hex) - 1, -1, -1):
        if hex[i] == 'A':
            result += val * 10
        elif hex[i] == 'B':
            result += val * 11
        elif hex[i] == 'C':
            result += val * 12
        elif hex[i] == 'D':
            result += val * 13
        elif hex[i] == 'E':
            result += val * 14
        elif hex[i] == 'F':
            result += val * 15
        else:
            result += val * int(hex[i])
        val *= 16

    print(result)