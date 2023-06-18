# import OS
import os

files = os.listdir()
for z, x in enumerate(files):
    print(f"{z}. {x}")
    # if x.endswith(".txt"):
    #     # Prints only text file present in My Folder
    #     print(x)

with open("read_exmple.txt", "r") as re:
    print(re.read())
