#for문을 이용하여 혈액형별 수

list = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

A_num = 0
O_num = 0
B_num = 0
AB_num = 0

for c in list:
    if c == 'A':
        A_num += 1
    elif c == 'B':
        B_num += 1
    elif c == 'O':
        O_num += 1
    else:
        AB_num += 1

print('{\'A\':', str(A_num)+',', '\'O\':', str(O_num)+',', '\'B\':', str(B_num)+',','\'AB\':', str(AB_num)+'}')