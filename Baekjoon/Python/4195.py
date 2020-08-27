def find(x):
    if x == friend[x]:
        return x
    else:
        parent = find(friend[x])
        friend[x] = parent
        return parent


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        friend[y] = x
        number[x] += number[y]


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        F = int(input())  # 친구 관계의 수
        friend = dict()
        number = dict()

        for _ in range(F):
            people_1, people_2 = map(str, input().split())
            if people_1 not in friend.keys():
                friend[people_1] = people_1
                number[people_1] = 1
            if people_2 not in friend.keys():
                friend[people_2] = people_2
                number[people_2] = 1

            union(people_1, people_2)
            print(number[find(people_1)])


