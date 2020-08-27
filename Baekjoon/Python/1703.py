if __name__ == "__main__":

    while True:
        tree = input()
        if tree[0] == '0':
            break
        else:
            tree = list(map(int, tree.split()))

            cnt = tree[1]
            flag = 1
            for i in range(2, tree[0] * 2 + 1):
                if flag:
                    cnt -= tree[i]
                    flag = 0
                else:
                    cnt *= tree[i]
                    flag = 1
        print(cnt)