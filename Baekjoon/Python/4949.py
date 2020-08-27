if __name__ == "__main__":

    while True:
        line = input()
        if line == ".":
            break
        else:
            stack = []
            flag = 1
            for i in range(len(line)):
                if line[i] in ["[", "("]:
                    stack.append(line[i])
                elif line[i] in ["]", ")"]:
                    if line[i] == "]":
                        if len(stack) == 0:
                            flag = 0
                            break
                        elif stack.pop() == "[":
                            continue
                        else:
                            flag = 0
                            break
                    else:
                        if len(stack) == 0:
                            flag = 0
                            break
                        elif stack.pop() == "(":
                            continue
                        else:
                            flag = 0
                            break
                else:
                    continue
            if flag == 1 and len(stack) == 0:
                print("yes")
            else:
                print("no")
