task5_file = open("task5_file.txt",'w+')
task5_file.write("Line---1\nLine---2\nLine---3\nLine---4\nLine---5\nLine---6\nLine---7\nLine---8\nLine---9\nLine--10\n")
task5_file.seek(0)
print("Before:\n" + task5_file.read() + "\n")
task5_file.close()

task5_file = open("task5_file.txt",'r+')

for item in range(1,2):
    task5_file.seek(0)
    task5_file.write("append#" + str(item) + "\n")
    
print(task5_file.read())

