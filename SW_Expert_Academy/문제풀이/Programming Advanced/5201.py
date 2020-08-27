if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N, K = map(int, input().split())
        w = list(map(int, input().split()))
        t = list(map(int, input().split()))
        total = 0
        visited = [0 for _ in range(len(t))]

        # 내림차순 정렬
        w.sort(reverse=True)
        t.sort(reverse=True)

        for i in range(len(w)):
            for j in range(len(t)):
                if t[j] >= w[i] and visited[j] == 0:
                    total += w[i]
                    visited[j] = 1
                    break

        if total == 0:
            print("#{0} 0".format(tc))
        else:
            print("#{0} {1}".format(tc, total))
