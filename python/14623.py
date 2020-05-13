def binaryToten(string):
    answer = 0
    val = 1
    for i in range(len(string) - 1, -1, -1):
        if string[i] == '1':
            answer += val
        val *= 2
    return answer


if __name__ == "__main__":

    n1 = input()
    n2 = input()

    n1 = binaryToten(n1)
    n2 = binaryToten(n2)

    n3 = n1 * n2

    result = []
    while n3 != 0:
        result.insert(0, n3 % 2)
        n3 //= 2

    print("".join(map(str, result)))
