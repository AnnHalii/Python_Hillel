
password: str = input('Input password:')
sign = {'@', '.', '!', '&', '?'}

if len(password) <= 8:
    print(f'Invalid')
elif not any(z in sign for z in password):
    print('Invalid')
elif not any([x.isdigit() for x in password]):
    print('Invalid')
elif not any([y.isalpha() for y in password]):
    print('Invalid')
elif not any([i.isupper() for i in password]):
    print('Invalid')
else:
    print('Accepted')
