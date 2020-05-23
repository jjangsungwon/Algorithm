if __name__ == "__main__":
    N = int(input())
    people = []
    for _ in range(N):
        name, kor, eng, math = map(str, input().split())
        people.append([name, int(kor), int(eng), int(math)])
    people = sorted(people, key=lambda x: (-x[1], x[2], -x[3], x[0]))

    for i in range(len(people)):
        print(people[i][0])
