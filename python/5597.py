import sys

if __name__ == "__main__":

    student = [0 for _ in range(31)]
    
    for i in range(28):
        check = int(input())
        
        student[check] = 1
    
    result = []
    for i in range(1, 31):
        if student[i] == 0:
            result.append(i)
    
    print(min(result))
    print(max(result))