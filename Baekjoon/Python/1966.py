if __name__ == "__main__":

    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())
        if N == 1:
            paper = int(input())
            print(1)
        else:
            cnt = 1
            paper = list(map(int, input().split()))
            for i in range(len(paper)):
                if i != M:
                    paper[i] = [paper[i], False]
                else:
                    paper[i] = [paper[i], True]

            flag = 1
            while flag:
                max_val = -1
                for i in range(len(paper)):
                    if paper[i][0] > max_val:
                        max_val = paper[i][0]

                for i in range(len(paper)):
                    if paper[0][0] != max_val:
                        val = paper.pop(0)
                        paper.extend([val])
                    else:
                        if paper[0][1] == True:
                            flag = 0
                            print(cnt)
                            break
                        else:
                            del paper[0]
                            break
                cnt += 1
