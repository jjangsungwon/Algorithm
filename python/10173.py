import sys

if __name__ == "__main__":
    
    
    while True:
        line = sys.stdin.readline().strip()
        check = 0
        if line == "EOI":
            break
        else:
            for i in range(len(line)-3):
                if line[i] == "N" or line[i] == "n":
                    if line[i+1] == "E" or line[i+1] == "e":
                        if line[i+2] == "M" or line[i+2] == "m":
                            if line[i+3] == "O" or line[i+3] == "o":
                                check = 1
                                break
            
            if check == 1:
                print("Found")
            else:
                print("Missing")