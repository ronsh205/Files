import os
import numpy as arr

files = os.listdir()
dic_path = {}
data = []
for num, file in enumerate(files):
    print(f"{num + 1}. {file}")
    dic_path[num + 1] = file
chose_user = int(input("enter number of file "))
file_user = dic_path[chose_user]
with open(file_user, 'r') as file_work:
    lines = file_work.readlines()
    for i in lines:
        data.append(i)
        print(i)
arr_file = arr.array(data)
print(f"arr_file is {arr_file}")
