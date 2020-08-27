TC = int(input())

for tc in range(1, TC + 1):
    Data = input()
    N = len(Data)
    stack = []

    for i in range(N):
        if Data[i] == "(" or Data[i] == "{":
            stack.append(Data[i])
        elif Data[i] == ")" or Data[i] == "}":
            if len(stack) == 0:
                stack = [Data[i]]
                break
            elif (Data[i] == "}" and stack[-1] != "{") or (Data[i] == ")" and stack[-1] != "("):
                stack = [Data[i]]
                break
            else:
                stack.pop()

    if not len(stack):
        print('#{0} 1'.format(tc))
    else:
        print('#{0} 0'.format(tc))