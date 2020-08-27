T = int(input())

operation = ["+", "-", "*", "/"]
for tc in range(1, T + 1):
    stack = []
    data = list(input().split())
    temp = 0

    for i in data:
        if i in operation:  # 연산자이면
            if len(stack) <= 1:
                print("#{0} error".format(tc))
                temp = 1
                break
            num1 = stack.pop()
            num2 = stack.pop()
            # num = str(eval(str(num1) + i + str(num2)))
            if i == operation[0]:
                num = num2 + num1
            elif i == operation[1]:
                num = num2 - num1
            elif i == operation[2]:
                num = num2 * num1
            elif i == operation[3]:
                num = num2 // num1
            stack.append(num)
        elif i == ".":
            if len(stack) == 1:
                print("#{0} {1}".format(tc, stack.pop()))
            else:
                print("#{0} error".format(tc))
                temp = 1
            break
        else:
            stack.append(int(i))

    if len(stack) >= 1 and temp != 1:
        print("#{0} error".format(tc))