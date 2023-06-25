import os

path_file = os.listdir()
files_work = {}


def init_dic():
    for num, file in enumerate(path_file):
        files_work[num + 1] = file
        print(f'{num} . {file}')


if __name__ == '__main__':
    init_dic()
    chose_user = int(input("enter number of file"))
    file_work = files_work[chose_user]
    data_file = input(f"insert data to file{file_work}\n")
    with open(file_work, 'a') as write_file:
        write_file.write('\n' + data_file)
