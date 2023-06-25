file1 = open("/home/ron/Documents/Mobiliay/File/Files/read_exmple.txt", 'r')
file2 = open("/home/ron/Documents/Mobiliay/File/Files/write_exmple.txt", 'r')
file3 = open("/home/ron/Documents/Mobiliay/File/Files/writecopy.txt", 'w')

for line1 in file1:
    for line2 in file2:
        if line1 == line2:
            file3.write(f'{line1}\n')
file1.close()
file2.close()
file3.close()
