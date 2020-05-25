import heapq, sys


if __name__ == "__main__":
    h = []
    heapq.heapify(h)
    for i in range(int(input())):
        n = int(sys.stdin.readline())
        if n == 0:
            if len(h) == 0:
                print(0)
            else:
                print(-1 * heapq.heappop(h))
        else:
            heapq.heappush(h, -n)

