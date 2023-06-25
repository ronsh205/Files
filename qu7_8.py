import os
import numpy as arr


def file_list(file_user):
    with open(file_user, 'r') as file_work:
        lines = file_work.readlines()
        for i in lines:
            data.append(i)
            print(i)
    arr_file = arr.array(data)
    print(f"arr_file is {arr_file}")
    return arr_file


def longest_word(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

files = os.listdir()
dic_path = {}
data = []
for num, file in enumerate(files):
    print(f"{num + 1}. {file}")
    dic_path[num + 1] = file
chose_user = int(input("enter number of file "))
file_user = dic_path[chose_user]

arr_user = file_list(file_user)
word_long = longest_word(file_user)
print(word_long)
