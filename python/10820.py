import sys

if __name__ == "__main__":
    
    while True:
        try:
            line = input()
        except:
            break
            
        num_cnt = 0
        num_empty = 0
        num_lower = 0
        num_upper = 0

        for i in range(len(line)):
            if line[i] == " ":
                num_empty += 1
            elif 48 <= ord(line[i]) <= 57:
                num_cnt += 1
            elif 97 <= ord(line[i]) <= 122:
                num_lower += 1
            elif 65 <= ord(line[i]) <= 90:
                num_upper += 1

        print(num_lower, num_upper, num_cnt, num_empty)
