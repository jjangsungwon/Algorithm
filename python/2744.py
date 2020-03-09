import sys

if __name__ == "__main__":

    string = input()
    result = []
    
    for i in range(len(string)):
        
        if 65 <= ord(string[i]) <= 90:
            result.append(chr(ord(string[i]) + 32))
        else:
            result.append(chr(ord(string[i]) - 32))
        
    print("".join(map(str, result)))
    