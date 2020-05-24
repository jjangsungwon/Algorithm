if __name__ == "__main__":

    string = input()
    stack = []

    val = 0
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(string[i])
        else:
            stack.pop()
            if string[i - 1] == "(":
                val += len(stack)
            else:
                val += 1
    print(val)
