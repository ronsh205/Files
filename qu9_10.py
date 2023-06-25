import os
import re

path_work = os.listdir()
dic_files = {}
dic_word = {}


def freq_words(file):
    result = []
    with open(file, 'r') as re_file:
        lines = re_file.readlines()
        for line in lines:
            # find all words
            words = re.compile('\w+', re.I)
            result = result + words.findall(line)
    for i in result:
        # insert dictionary all words and count
        if i in dic_word:
            dic_word[i] += 1
        else:
            dic_word[i] = 1


for num, file in enumerate(path_work):
    dic_files[num + 1] = file
    print(f"{num + 1} {file}")
chose_user = int(input("enter number file you chose "))
file_work = dic_files[chose_user]
# get size of file
size_file = os.path.getsize(file_work)
print(file_work)
print(f'numer lines is {num + 1} ')
freq_words(file_work)
print(dic_word)
print(f"size file you chose {size_file} bytes")
