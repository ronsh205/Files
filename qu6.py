import os

# open path Absolutely with system call
files = os.listdir()
# define dictionary to initialize file and number
dic_path = {}
for num, file in enumerate(files):
    print(f"{num + 1} . {file}")
    dic_path[num + 1] = file
#     chose from user the file
chose_user = int(input("enter number of file "))
# open to read file
with open(dic_path[chose_user], 'r') as re:
    read_file = re.readline()
    for line in read_file:
        data = line
        print(data)
