
password: str = input('Input password:')
sign = {'@', '.', '!', '&', '?'}

if len(password) <= 8:
    raise ValueError
elif not any(z in sign for z in password):
    raise KeyError
elif password.isdigit():
    raise AttributeError
elif password.isalpha():
    raise AttributeError
elif password.isupper():
    raise AttributeError
else:
    print('Accepted')
