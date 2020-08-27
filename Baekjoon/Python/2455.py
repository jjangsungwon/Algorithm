
if __name__ == "__main__":
    data = []
    
    for i in range(4):
        data_list = list(map(int, input().split()))
        data.append(data_list)
        
    max_people = 0
    people = 0
    for i in range(4):
        people -= data[i][0]
        people += data[i][1]
        
        if people > max_people:
            max_people = people
    
    print(max_people)