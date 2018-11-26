// input파일은 다음과 같음
//A,A,0
//A,B,570
//A,C,1000
//A,D,510
//A,E,270
//A,F,870
//A,G,830
//B,B,0
//B,C,430
//B,D,60
//B,E,300
//B,F,300
//B,G,260
//C,C,0
//C,D,490
//C,E,730
//C,F,130
//C,G,170
//D,D,0
//D,E,240
//D,F,360
//D,G,320
//E,E,0
//E,F,600
//E,G,560
//F,F,0
//F,G,40
//G,G,0
//위와 같이 Station 이름과 각 Station사이의 Distance가 기록되어있는 파일을 읽어와 Station 순서를 파악
//시작 Station이 될 수 있는 station이 하나 이상일 경우 알파벳 순서로 정함

info = open("input.txt",'r')
info_lst = []
station_lst = []
station_value = []
for line in info:
    info_lst = line[:-1].split(",")
    if info_lst[1] not in station_lst:
        station_lst.append(info_lst[1])
        station_value.append(0)


    index1 = station_lst.index(info_lst[0])
    index2 = station_lst.index(info_lst[1])
    
    if info_lst[0] == station_lst[0]:
        station_value[index2] = int(info_lst[2]) - station_value[index1]
      
    else:
        if info_lst[0] != info_lst[1]:
            if int(info_lst[2]) > abs(station_value[index1] - station_value[index2]):
                station_value[index2] -= int(info_lst[2])

output_lst = []
station_value_remove = station_value[:]

while station_value_remove != []:
    min = station_value_remove[0]
    for value in station_value_remove:
        if min > value:
            min = value
    index = station_value.index(min)
    output_lst.append(station_lst[index])
    station_value_remove.remove(min)

if output_lst[0] > output_lst[-1]:
    print(output_lst[::-1])
else:
    print(output_lst)

info.close()
