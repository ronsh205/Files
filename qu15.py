import os
import random

path_file = os.listdir()
files_work = {}


def init_dic():
    for num, file in enumerate(path_file):
        files_work[num + 1] = file
        print(f'{num + 1} . {file}')


if __name__ == '__main__':
    init_dic()
    chose_user = int(input("enter number of file"))
    file_work = files_work[chose_user]

    with open(file_work, 'r') as re:
        Lines = re.readlines()
        size_lines = len(Lines)
        print(size_lines)
        line_ran = random.randint(0, 7)
        for num, line in enumerate(Lines):
            data = line
            if num == line_ran:
                break

        print(data)
