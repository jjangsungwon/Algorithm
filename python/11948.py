if __name__ == "__main__":

    score = []
    for _ in range(6):
        score.append(int(input()))

    first = score[:4]
    second = score[4:]

    first.sort(reverse=True)
    second.sort(reverse=True)

    total = sum(first[:3]) + second[0]
    print(total)