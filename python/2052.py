import decimal

if __name__ == "__main__":

    N = int(input())
    result = 1
    for i in range(N):
        result *= 2

    result = list(str(decimal.Decimal(1 / result)))

    if 'E' in result:
        index = result.index('E')
        val = int(result[index + 2] + result[index + 3])
        del result[index:]

        first = result.pop(0)
        result.insert(0, 0)
        result.insert(2, first)
        for i in range(val - 1):
            result.insert(2, 0)

    print("".join(map(str, result)))
