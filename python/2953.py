import sys

if __name__ == "__main__":
    person = []
    
    # input
    for i in range(5):
        person.append(list(map(int, sys.stdin.readline().split())))
    
    
    max_index, max_value = 0, 0
    for i in range(5):
        if sum(person[i]) > max_value:
            max_value, max_index = sum(person[i]), i + 1
     
    print(max_index, max_value)
    