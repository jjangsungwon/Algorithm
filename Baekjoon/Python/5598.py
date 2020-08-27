import sys

if __name__ == "__main__":
    data = input()
    result = [0 for _ in range(len(data))]
    
    for i in range(len(data)):
        if ord(data[i]) <= 67:
            result[i] = chr(ord(data[i]) + 23)
        else:
            result[i] = chr(ord(data[i]) - 3)
    
    print("".join(result))