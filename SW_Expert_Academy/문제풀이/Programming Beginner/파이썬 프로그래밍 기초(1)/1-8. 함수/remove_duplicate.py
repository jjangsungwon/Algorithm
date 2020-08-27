# 리스트 중복(duplication) 제거

def remove_duplicate(n):
    return list(set(n))


ex_list = [1, 2, 3, 4, 3, 2, 1]
print(ex_list)
print(remove_duplicate(ex_list))
