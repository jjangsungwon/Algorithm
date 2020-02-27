import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    # 밑면 n * 2
    # 옆면 n * 2
    # 반쪽 짤긴거 (n-1)/2 * 2
    # 윗면 1
    # 다 더하면 4n
    print(n * 4)
