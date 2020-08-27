#list 내포 기능을 이용하여 문장 내 모음(aeiou) 제거

vowel = "aeiou"
sentence = "Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open."

result = [char for char in sentence if char not in vowel]

print(''.join(result))