import itertools


def condition(data):
    vowel = ['a', 'e', 'i', 'o', 'u']
    vowel_cnt, consonant_cnt = 0, 0

    for i in data:
        if i in vowel:
            vowel_cnt += 1
        else:
            consonant_cnt += 1

        if vowel_cnt >= 1 and consonant_cnt >= 2:
            return 1
    return 0


if __name__ == "__main__":
    # input
    L, C = map(int, input().split())
    arr = list(input().split())
    arr.sort()

    # sort
    data = list(itertools.combinations(arr, L))

    for i in data:
        if condition(i):
            print("".join(map(str, i)))
