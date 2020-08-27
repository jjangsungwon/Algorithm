if __name__ == "__main__":

    T = int(input())

    for _ in range(T):
        x, y = map(int, input().split())
        sub = y - x

        init, val, cnt = 3, 2, 3
        flag = 1

        if sub <= 2:
            print(sub)
        else:
            while flag:
                for _ in range(2):
                    if init <= sub < init + val:
                        flag = 0
                        print(cnt)
                        break
                    else:
                        init += val
                        cnt += 1
                val += 1