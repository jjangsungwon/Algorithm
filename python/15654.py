import itertools


if __name__ == "__main__":

    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    result = list(itertools.permutations(num_list, M))
    result.sort()

    for i in range(len(result)):
        print(" ".join(map(str, result[i])))