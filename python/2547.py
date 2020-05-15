if __name__ == "__main__":

    T = int(input())

    for _ in range(T):
        input()
        N = int(input())
        student = []
        for _ in range(N):
            student.append(int(input()))

        if sum(student) % len(student) == 0:
            print("YES")
        else:
            print("NO")