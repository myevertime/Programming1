import numpy as np

text = open("input.txt", encoding = 'utf-8-sig')
nameList = open("nameList.txt", encoding = 'utf-8-sig')

// input파일에는 법안번호, 정치인 이름, 찬성/반대/기권 로 구성되어있음 ("000001,홍길동,찬성")
// nameList파일에는 정당과 정치인 이름이 적혀있음

name_lst = []
bill_lst= []
index = 0
lst = []

name = nameList.readline()
while name !="":
    if '\n' in name:
        name_lst.append(name[:-1])
    else:
        name_lst.append(name)
    name = nameList.readline()
    
for i in range(len(name_lst)):
    lst.append([])

line = text.readline()
while line != "":
    if line == '\n':
        line = text.readline()
    person = line[:-1].split(",")
    if person == ['']:
        break;

    if person[0] not in bill_lst:
        bill_lst.append(person[0])
    
    if person[1] == name_lst[index]:
        if person[2] == '찬성':
            lst[index].append(1)
        elif person[2] == '기권':
            lst[index].append(0)
        else:
            lst[index].append(-1)

    if person[1] > name_lst[index]:
        index += 1
        
        if index == len(name_lst):
            index = 0
        else:
            continue
    else:
        index += 1
    
    if index == len(name_lst):
        index = 0
        for i in range(len(lst)):
            if len(lst[i]) != len(bill_lst):
                lst[i].append(0)

    line = text.readline()

lst = np.array(lst)
lst2 = lst.transpose()
result = np.matmul(lst,lst2)
result.astype(int)

text.close()
nameList.close()

np.savetxt("output_8_3.txt", result, fmt='%i', delimiter=',')
