import sys

if __name__ == "__main__":

    while True:
        line = list(map(str, sys.stdin.readline()))
        line.pop()
        if line[0] == 'E' and line[1] == 'N' and line[2] == 'D':
            break
        else:
            line.reverse()
            print("".join(line))
