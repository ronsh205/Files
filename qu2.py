import os

Dic_lis = {}
files = os.listdir()
for z, x in enumerate(files):
    print(f"{z + 1}. {x}")
    Dic_lis[z + 1] = x

chose_user = int(input("enter number of line file\n"))
print("the file work with is :\n" + Dic_lis[chose_user])
file_work = Dic_lis[chose_user]
with open(file_work, 'r') as re:
    Lines = re.readlines()
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        print("Line {}: {}".format(count, line.strip()))
