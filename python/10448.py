import itertools


if __name__ == "__main__":

    T = int(input())
    n = []

    for i in range(1, 50):
        n.append(i * (i + 1) // 2)

    n = list(itertools.combinations_with_replacement(n, 3))

    for _ in range(T):
        k = int(input())

        for i in range(len(n)):
            if sum(n[i]) == k:
                print(1)
                break
            elif i == len(n) - 1:
                print(0)