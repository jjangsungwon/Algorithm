import itertools

if __name__ == "__main__":

    while True:
        try:
            data = list(map(int, input().split()))

            k = data.pop(0)

            result = itertools.combinations(data, 6)

            for i in result:
                print(" ".join(map(str, i)))
            print("")
        except:
            break
