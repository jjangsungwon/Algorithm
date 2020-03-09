if __name__ == "__main__":
    
    result = []
    
    for i in range(1, 6):
        name = input()
        
        if "FBI" in name:
            result.append(i)
            
    
    if len(result) == 0:
        print("HE GOT AWAY!")
    else:
        print(" ".join(map(str, result)))