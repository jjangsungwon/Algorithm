import heapq
import sys



"""

[1, 2] : 최대 힙
[3] : 최소 힙



"""


if __name__ == "__main__":

    t = int(sys.stdin.readline())
    for _ in range(t):
        m = int(sys.stdin.readline())
        array = list()
        if m % 10 == 0:
            for _ in range(m // 10):
                array.extend(list(map(int, sys.stdin.readline().split())))
        else:
            for _ in range(m // 10 + 1):
                array.extend(list(map(int, sys.stdin.readline().split())))

        max_heap, min_heap = list(), list()
        count = 0
        result = []
        for i in range(m):
            if len(max_heap) == 0 and len(min_heap) == 0:
                heapq.heappush(max_heap, -array[i])
            elif len(max_heap) == len(min_heap):
                if min_heap[0] < array[i]:
                    temp = heapq.heappop(min_heap)
                    heapq.heappush(max_heap, -temp)
                    heapq.heappush(min_heap, array[i])
                else:
                    heapq.heappush(max_heap, -array[i])
            elif len(max_heap) > len(min_heap):
                if -max_heap[0] > array[i]:
                    temp = heapq.heappop(max_heap)
                    heapq.heappush(max_heap, -array[i])
                    heapq.heappush(min_heap, -temp)
                else:
                    heapq.heappush(min_heap, array[i])
            if i % 2 == 0:
                count += 1
                result.append(-max_heap[0])

        print(count)
        cnt = 0
        for i in range(count):
            cnt += 1
            if cnt % 10 == 0 or i == count - 1:
                print(result[i])
            else:
                print(result[i], end=' ')
