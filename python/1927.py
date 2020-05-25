import heapq,sys


if __name__ == "__main__":
    N = int(input())
    h = []
    heapq.heapify(h)
    for _ in range(N):
        num = int(sys.stdin.readline())

        if num == 0:
            if len(h) == 0:
                print(0)
            else:
                print(heapq.heappop(h))
        else:
            heapq.heappush(h, num)

