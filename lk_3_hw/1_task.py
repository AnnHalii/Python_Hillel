import sys


first_value: str = input('Input first value: ')
operation: str = input('Input math operation: ')
second_value: str = input('Input second value: ')

try:
    first_value: int = int(first_value)
    second_value: int = int(second_value)
except ValueError:
    print('ValueError')
    sys.exit(0)

if operation == '+':
    print(first_value + second_value)
elif operation == '-':
    print(first_value - second_value)
elif operation == '*':
    print(first_value * second_value)
elif operation == '/':
    try:
        print(first_value / second_value)
    except ZeroDivisionError:
        print(f'Incorrect second value!: {second_value}')

elif operation == '//':
    try:
        print(first_value // second_value)
    except:
        print(f'Incorrect second value: {second_value}')
elif operation == '**':
    print(first_value ** second_value)
