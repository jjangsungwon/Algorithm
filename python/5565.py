import sys

if __name__ == "__main__":
    
    total = int(input())
    book = []
    
    for i in range(9):
        book.append(int(input()))
        
    print(total - sum(book))