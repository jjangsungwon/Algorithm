# 대문자 -> 소문자, 소문자 -> 대문자, 알파벳이 아닐 경우에 그냥 출력

c = input()

if ord(c) >= ord('a'):
    print(c + '(ASCII:', str(ord(c))+') =>', c.upper() + '(ASCII:', str(ord(c.upper()))+')')
elif ord(c) >= ord('A'):
    print(c + '(ASCII:', str(ord(c))+') =>', c.lower() + '(ASCII:', str(ord(c.lower()))+')')
else:
    print(c)
