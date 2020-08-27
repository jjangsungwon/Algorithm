if __name__ == "__main__":
    
    grade = input()
    result = 0.0
    
    if grade[0] == "A":
        result += 4
    elif grade[0] == "B":
        result += 3
    elif grade[0] == "C":
        result += 2
    elif grade[0] == "D":
        result += 1
    else:
        print(result)
        exit()
    
    if grade[1] == "+":
        result += 0.3
    elif grade[1] == "-":
        result -= 0.3
        
    print(result)