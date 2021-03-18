import sys

first_value: str = input('Input first value: ')
operation: str = input('Input math operation: ')
second_value: str = input('Input second value: ')

for value in {first_value, second_value}:
    if not value.isdigit():
        print(f'Value of type {type(value)} {value} is not a digit')
        sys.exit(0)
    first_value: int = int(first_value)
    second_value: int = int(second_value)

if operation == '+':
    print(first_value + second_value)
elif operation == '-':
    print(first_value - second_value)
elif operation == '*':
    print(first_value * second_value)
elif operation == '/' and second_value != 0:
    print(first_value / second_value)
elif operation == '%' and second_value != 0:
    print(first_value % second_value)
elif operation == '**':
    print(first_value ** second_value)
else:
    print(f'Invalid operation {operation}')