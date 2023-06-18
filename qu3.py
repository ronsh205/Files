import os


def file_app():
    Dic_lis = {}
    files = os.listdir()
    for z, x in enumerate(files):
        print(f"{z + 1}. {x}")
        Dic_lis[z + 1] = x

    chose_user = int(input("enter number of line file\n"))
    print("the file work with is :\n" + Dic_lis[chose_user])
    file_work = Dic_lis[chose_user]
    with open(file_work, 'a') as write_file:
        data = input("enter data want append  ")
        data = '\n' + data
        write_file.write(data)


if __name__ == '__main__':
    file_app()
