if __name__ == "__main__":

    while True:
        a, b = map(str, input().split())

        if int(a) + int(b) == 0:
            break

        cnt, flag = 0, 0
        for i in range(-1, -min(len(a), len(b)) - 1, -1):
            if flag == 1:
                if int(a[i]) + int(b[i]) >= 9:
                    cnt += 1
                else:
                    flag = 0
            else:
                if int(a[i]) + int(b[i]) >= 10:
                    cnt += 1
                    flag = 1
                else:
                    flag = 0
        if len(a) > len(b):
            for i in range(-len(b) - 1, -len(a) - 1, -1):
                if flag == 1:
                    if int(a[i]) + flag >= 10:
                        cnt += 1
                    else:
                        flag = 0
                else:
                    break
        elif len(a) < len(b):
            for i in range(-len(a) - 1, -len(b) - 1, -1):
                if flag == 1:
                    if int(b[i]) + flag >= 10:
                        cnt += 1
                    else:
                        flag = 0
                else:
                    break
        print(cnt)
