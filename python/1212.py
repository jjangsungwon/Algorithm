import sys

octal = ["000", "001", "010", "011", "100", "101", "110", "111"]
octal_1 = ["", "1", "10", "11", "100", "101", "110", "111"]

o_num = sys.stdin.readline()

if int(o_num) == 0:
    print(0)
else:
    print(octal_1[int(o_num[0])], end="")
    for i in range(1, len(o_num) - 1):
        print(octal[int(o_num[i])], end="")
