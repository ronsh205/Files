import os

Dic_lis = {}
files = os.listdir()
for z, x in enumerate(files):
    print(f"{z + 1}. {x}")
    Dic_lis[z + 1] = x

chose_user = int(input("enter number of line file\n"))
print(Dic_lis[chose_user])
