!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt

mean_temp_file = open("mean_temp.txt", 'a+')
mean_temp_file.write("Rio de Janeiro,Brazil,30.0,18.0\n")
mean_temp_file.close()

mean_temp = open("mean_temp.txt",'r')
headings = mean_temp.readline()
print(headings)

print(headings.split(','))

city_temp = mean_temp.readline()
count1 = 0
count2 = 2
while city_temp :
    city_list = city_temp.split(',')
    print("\"month ave: highest high\" for ", city_list[count1], "is", city_list[count2])
    city_temp = mean_temp.readline()
