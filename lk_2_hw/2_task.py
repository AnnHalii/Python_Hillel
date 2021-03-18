
password: str = input('Input password:')
sign = {'@', '.', '!', '&', '?'}

if len(password) <= 8:
    print(f'Invalid')
elif not any(z in sign for z in password):
    print('Invalid')
elif password.isdigit():
    print('Invalid')
elif password.isalpha():
    print('Invalid')
elif password.isupper():
    print('Invalid')
else:
    print('Accepted')
