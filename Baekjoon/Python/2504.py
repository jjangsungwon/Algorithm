if __name__ == "__main__":
    
    data = list(input())
    stack = list()
    
    for i in data:
        val = 0
        if i == ")":
            while stack:
                top = stack.pop()
                if top == "(":
                    if val == 0:
                        stack.append(2)
                    else:
                        stack.append(2 * val)
                    break
                elif top == "[":
                    print(0)
                    exit()
                else:
                    val += int(top)
        elif i == "]":
            while stack:
                top = stack.pop()
                if top == "[":
                    if val == 0:
                        stack.append(3)
                    else:
                        stack.append(3 * val)
                    break
                elif top == "(":
                    print(0)
                    exit()
                else:
                    val += int(top)
        else:
            stack.append(i)
        
    result = 0
    for i in stack:
        if i == "(" or i == "[" or i == ")" or i =="]":
            print(0)
            exit()
        else:
            result += i
    
    print(result)
        
    
    