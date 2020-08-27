import sys

if __name__ == "__main__":
    set = [0] * 21

    T = int(sys.stdin.readline())

    for i in range(T):
        instruct, *num = sys.stdin.readline().split()

        if len(num) > 0:
            num = int(num[0])

        if instruct == "add":
            set[num] = 1
        elif instruct == "remove":
            set[num] = 0
        elif instruct == "check":
            print(set[num])
        elif instruct == "toggle":
            if set[num]:
                set[num] = 0
            else:
                set[num] = 1
        elif instruct == "empty":
            set = [0] * 21
        elif instruct == "all":
            set = [1] * 21