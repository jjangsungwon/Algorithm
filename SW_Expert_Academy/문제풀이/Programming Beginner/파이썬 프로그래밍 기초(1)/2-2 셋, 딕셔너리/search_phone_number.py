#검색할 수 있는 데이터 목록
ex_data = {'홍길동':'010-1111-1111',
           '이순신':'010-1111-2222',
           '강감찬':'010-1111-3333'
           }

# key data 모음
key_data = ex_data.keys()

print('아래 학생들의 전화번호를 조회할 수 있습니다.')

# keky data 출력
for student in key_data:
    print(student)

# 전화번호를 조회하고자 하는 이름 입력
print('전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.')
name = input()
print('{0}의 전화번호는 {1}입니다.'.format(name, ex_data[name]))
