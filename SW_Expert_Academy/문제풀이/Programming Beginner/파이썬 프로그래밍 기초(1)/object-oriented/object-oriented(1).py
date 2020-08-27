class subject:
    korean = 0
    english = 0
    math = 0

    def assign(self, korean, english, math):
        self.korean = korean
        self.english = english
        self.math = math

    def total(self):
        return self.korean + self.english + self.math

    def print(self):
        print('국어, 영어, 수학의 총점: {0}'.format(self.korean + self.english + self.math))


# score = list(map(int, sys.stdin.readline().split(',')))

score = list(map(int, input().split(',')))
subject = subject()
subject.assign(score[0], score[1], score[2])
subject.print()