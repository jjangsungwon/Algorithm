hexa = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        n, h = input().split()
        arr = []
        for i in range(int(n)):
            b = h[i]

            if ord(b) < ord('A'):
                arr.append(hexa[int(b)])
            else:
                arr.append(hexa[ord(b) - 55])

        print("#{0} ".format(tc) + "".join(arr))


