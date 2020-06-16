import sys

sys.setrecursionlimit(10 ** 6)


if __name__ == "__main__":

    T = int(input())
    for _ in range(T):
        N = int(input())
        p = list(map(int, input().split()))
        p.insert(0, 0)  # 인덱스 편의를 위해서 삽입
        team = [0] * (N + 1)

        for i in range(1, N + 1):
            if team[i] == 0:  # 아직 팀이 없는 경우
                team_number = i
                # 팀 구성한다고 가정
                while team[i] == 0:
                    team[i] = team_number
                    i = p[i]
                # 역순으로 순환하면서 사이클 확인
                while team[i] == team_number:
                    team[i] = -1
                    i = p[i]
        result = N - team.count(-1)
        print(result)
