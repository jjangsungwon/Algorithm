import sys

alphabet = [0 for _ in range(26)]

if __name__ == "__main__":
    str_list = sys.stdin.readline().strip()
    
    
    for i in range(len(str_list)):
        alphabet[ord(str_list[i]) - 97] += 1
        
    
    print(" ".join(map(str, alphabet)))