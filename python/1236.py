from collections import defaultdict

if __name__ == "__main__":
    N, M = map(int, input().split())
    data = [list(map(str, input().strip())) for _ in range(N)]

    # 행에서 경비원이 없는 구간 파악
    row_dic = defaultdict(int)
    for i in range(N):
        if 'X' in data[i]:
            row_dic[i] = 1
        else:
            row_dic[i] = 0

    # 열에서 경비원이 없는 구간 파악
    col_dic = defaultdict(int)
    for i in range(M):
        flag = False
        for j in range(N):
            if 'X' == data[j][i]:
                col_dic[i] = 1
                flag = True
                break
        if not flag:
            col_dic[i] = 0

    # 둘 다 비어있는 부분 파악(교집합)
    row_empty = set()
    for key in row_dic.keys():
        if row_dic[key] == 0:
            row_empty.add(key)

    col_empty = set()
    for key in col_dic.keys():
        if col_dic[key] == 0:
            col_empty.add(key)

    # 출력
    print(max(len(row_empty), len(col_empty)))


