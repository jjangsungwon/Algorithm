# 회문

def palindrome(str):
    return list(reversed(str))
    #return str.reverse() reverse는 return 값이 없다


string = list(input())
reverse = palindrome(string)

print("".join(map(str, reverse)))
if string == reverse:
    print('입력하신 단어는 회문(Palindrome)입니다.')
