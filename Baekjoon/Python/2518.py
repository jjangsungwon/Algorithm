import sys
import copy

sys.setrecursionlimit(10 ** 8)
N = int(sys.stdin.readline())
K = int(N / 3)
dad = list(map(int, sys.stdin.readline().split()))
mother = list(map(int, sys.stdin.readline().split()))
hyun = list(map(int, sys.stdin.readline().split()))

dad_position = 1
mother_position = K + 1
hyun_position = 2 * K + 1
count = 0
real_move = 1000000
move = 0
goal = int(dad[0]) + int(mother[0]) + int(hyun[0])


def dfs(count, move, dad_position, mother_position, hyun_position, dad, mother, hyun):
    global real_move

    if move >= 30:
        return

    dad_copy = copy.deepcopy(dad)
    mother_copy = copy.deepcopy(mother)
    hyun_copy = copy.deepcopy(hyun)

    if dad_position in dad_copy:
        count += 1
        dad_copy.remove(dad_position)

    if mother_position in mother_copy:
        count += 1
        mother_copy.remove(mother_position)

    if hyun_position in hyun_copy:
        count += 1
        hyun_copy.remove(hyun_position)

    if count == goal:
        if real_move > move:
            real_move = move
            return

    dfs(count, move+1, int((dad_position + 1) % N), int((mother_position + 1) % N), int((hyun_position + 1) % N),
        dad_copy, mother_copy, hyun_copy)
    dfs(count, move+1, int((dad_position - 1) % N), int((mother_position - 1) % N), int((hyun_position - 1) % N),
        dad_copy, mother_copy, hyun_copy)


dfs(0, 0, dad_position, mother_position, hyun_position, dad[1:], mother[1:], hyun[1:])

print(real_move)
