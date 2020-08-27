class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return "이름: {0}".format(self.name)


class GraduateStudent(Student):
    def __init__(self, name, major):
        super().__init__(name)
        self.__major = major

    @property
    def major(self):
        return self.__major

    def __repr__(self):
        return super().__repr__() + ", 전공: {0}".format(self.major)


s1 = Student("홍길동")
s2 = GraduateStudent("이순신", "컴퓨터")
print(s1)
print(s2)
