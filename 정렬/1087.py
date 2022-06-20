import sys


if __name__ == "__main__":
  n = int(sys.stdin.readline())
  arr = list(map(int, sys.stdin.readline().split()))

  # 중복 제거
  arr = list(set(arr))

  # 정렬
  arr.sort()

  print(" ".join(map(str, arr)))