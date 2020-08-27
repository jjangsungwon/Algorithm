TC = int(input())

for tc in range(1, TC + 1):
    string = input()
    length = len(string)

    while True:
        result = 0
        for i in range(1, len(string)):
            if string[i] == string[i - 1]:
                string = string[: i - 1] + string[i + 1:]
                result = 1
                break

        if result == 0:
            break

    print('#{0} {1}'.format(tc, len(string)))
