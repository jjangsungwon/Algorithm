# input
N = int(input())

temp = 1


def dfs(count, value):
    while True:
        # print('count : {0} value : {1}'.format(count, value))

        data = str(value)
        check = 0
        pre = 0
        for i in range(len(str(value))):
            if data[i] == '6':
                check += 1
            else:
                check = 0

            if check >= 3:
                count += 1

                if count == N:
                    print(value)
                    exit()
                break

        value += 1


dfs(0, 666)
