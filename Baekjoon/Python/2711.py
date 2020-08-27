
if __name__ == "__main__":
    
    T = int(input())
    
    for i in range(T):
        n, string = input().split()
        n = int(n)
        string = list(string)
        
        del string[n-1]
        print("".join(map(str, string)))
        