with open('new.txt', "r") as file:
    print(file.read())


with open('new.txt') as file_read, open('new_file.txt', 'w') as file_write:
    file_write.write(file_read.read())

with open('test.txt', 'r+') as file:
    data = file.read()
    file.write('!'.join(data.split(',')))


