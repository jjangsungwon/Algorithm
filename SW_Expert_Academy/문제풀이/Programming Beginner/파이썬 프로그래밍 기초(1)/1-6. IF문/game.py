# 가위바위보

game = ["가위", "바위", "보"]

Man1 = input()
Man2 = input()

if Man1 == game[0]:
    if Man2 == game[0]:
        print('Result : Draw')
    elif Man2 == game[1]:
        print('Result : Man2 Win!')
    else:
        print('Result : Man1 Win!')
elif Man1 == game[1]:
    if Man2 == game[1]:
        print('Result : Draw')
    elif Man2 == game[2]:
        print('Result : Man2 Win!')
    else:
        print('Result : Man1 Win!')
elif Man1 == game[2]:
    if Man2 == game[2]:
        print('Result : Draw')
    elif Man2 == game[1]:
        print('Result : Man2 Win!')
    else:
        print('Result : Man1 Win!')