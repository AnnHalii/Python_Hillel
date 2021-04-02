file = input('Enter name of file:')
if '.' not in file:
    raise BaseException('Incorrect name of file')
else:
    print(file.split('.')[-1])
