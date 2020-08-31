import heapq

if __name__ == "__main__":
    n = int(input())  # 주유소의 개수
    q = []
    for _ in range(n):
        distance, cost = map(int, input().split())
        heapq.heappush(q, (-cost, distance))
    l, p = map(int, input().split())  # 마을까지의 거리, 원래 있던 연료의 양

    if p >= l:
        print(0)
    else:
        # 이동 시작
        cnt = 0
        location = 0  # 현재 위치
        sub_q = []
        temp = []
        while True:
            # 갈 수 있는 거리에 있는 위치 찾기
            while q:
                cost, distance = heapq.heappop(q)
                if distance <= location + p:
                    heapq.heappush(sub_q, (cost, distance))
                else:  # 갈 수 없으면
                    heapq.heappush(temp, (distance, cost))

            if len(sub_q) == 0:  # 갈 수 있는 곳이 없는 상황
                break

            # 갈 수 있는 곳에서 제일 연료량이 높은 것 출력
            cost, distance = heapq.heappop(sub_q)
            cost = -cost
            if location < distance:  # 더 먼 곳이면
                p = p - (distance - location) + cost
                location = distance  # 위치 업데이트
            else:
                p += cost  # 비용만 업데이트
            cnt += 1

            if location + p >= l:  # 갈 수 있다면
                print(cnt)
                exit()

            q.extend(sub_q)  # sub_q -> q

            # temp 중에 갈 수 있는거 q로 옮기기
            while temp:
                distance, cost = heapq.heappop(temp)
                if distance <= location + p:
                    heapq.heappush(q, (cost, distance))
                else:
                    heapq.heappush(temp, (distance, cost))
                    break
            sub_q = []

        # 갈 수 없는 경우
        print(-1)