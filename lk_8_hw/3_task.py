from collections import Counter


def converter(string, separator):
    c = Counter()
    for word in string.split(separator):
        c[word] += 1
    return dict(c)


my_str = input('String')
delimiter = input('delimiter')

print(converter(my_str, delimiter))
