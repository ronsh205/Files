import os

Dic_lis = {}
files = os.listdir()
for z, x in enumerate(files):
    print(f"{z + 1}. {x}")
    Dic_lis[z + 1] = x

chose_user = int(input("enter number of line file\n"))
data_list = []
file_work = Dic_lis[chose_user]
print("the file work with is :\n" + Dic_lis[chose_user])
with open(file_work, 'r') as re:
    Lines = re.readlines()
    for line in Lines:
        data_list.append(line)
print("the list is ")
for step in data_list:
    print(step)
