from collections import defaultdict


if __name__ == "__main__":
    # inputs
    N = int(input())  # 크레인 갯수
    crane = list(map(int, input().split()))
    M = int(input())  # 상자 갯수
    box = list(map(int, input().split()))

    # 내림차순 정렬
    crane.sort(reverse=True)
    box.sort(reverse=True)

    # 탐색 시작(그리디)
    if max(box) > max(crane):  # 담을 수 없는 경우
        print(-1)
    else:
        answer = 0
        # 각 크레인이 담을 수 있는 상자 정보 저장
        crane_dic = defaultdict(list)
        for i in range(N):
            for j in range(M):
                if crane[i] >= box[j]:
                    crane_dic[crane[i]].append(j)

        # 탐색
        answer = 0
        count = 0
        box_flag = [0] * M
        while count != M:
            answer += 1
            for i in range(N):
                for j in crane_dic[crane[i]]:
                    if box_flag[j] == 0:
                        box_flag[j] = 1
                        count += 1
                        break
        print(answer)