if __name__ == "__main__":

    while True:
        num = input()

        if num == "-1":
            break
        else:
            num = list(map(int, num.split(" ")))

            cnt = 0
            for i in range(len(num) - 1):
                if num[i] * 2 in num:
                    cnt += 1
            print(cnt)