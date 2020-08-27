if __name__ == "__main__":

    score = list(map(int, input().split()))

    print(abs(score[3] + score[0] - score[2] - score[1]))