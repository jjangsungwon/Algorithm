def stars(star, idx):
    global k, result

    if idx == k:
        result = star
    else:
        temp, value = [], len(star)
        for i in range(3 * value):
            if i // value == 1:
                temp.append(star[i % value] + " " * value + star[i % value])
            else:
                temp.append(star[i % value] * 3)
        stars(temp, idx + 1)


if __name__ == "__main__":

    n = int(input())
    star = ["***", "* *", "***"]
    k = 0
    result = []

    while n != 3:
        n //= 3
        k += 1

    stars(star, 0)
    for i in result:
        print(i)
