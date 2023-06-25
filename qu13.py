import shutil
import os

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
    destination = "/home/ron/Documents/Mobiliay/File/Files/"
    name_file = input("what name file ") + '.py'
    destination += name_file
    shutil.copyfile(file_work, destination)
