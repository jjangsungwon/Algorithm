# 대소문자 구분

c = input()

#print(ord('a')) #문자 -> 아스키
#print(chr(65)) #아스키 -> 문자

if ord(c) >= ord('a'):
    print(c,'는 소문자 입니다.')