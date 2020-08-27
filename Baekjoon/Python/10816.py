from sys import stdin
from collections import Counter

if __name__ == "__main__":

    N = int(stdin.readline())
    N_list = list(map(int, stdin.readline().split()))
    M = int(stdin.readline())
    M_list = list(map(int, stdin.readline().split()))

    c = Counter(N_list)

    for i in range(len(M_list)):
        print(c[M_list[i]], end=" ")
