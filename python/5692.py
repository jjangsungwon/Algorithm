import math


if __name__ == "__main__":

    while True:
        N = input()
        if N == '0':
            break
        else:
            total, val = 0, 1
            for i in range(-1, -len(N) -1, -1):
                total += int(N[i]) * math.factorial(val)
                val += 1
            print(total)