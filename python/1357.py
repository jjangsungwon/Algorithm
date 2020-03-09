if __name__ == "__main__":

    n = input().split()
    print(int(str(int(n[0][::-1])+int(n[1][::-1]))[::-1]))