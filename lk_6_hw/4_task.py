def parse(string):
    b = 0
    res = []
    for i in list(string):
        if i == 'i':
            b += 1
        elif i == 'd':
            b -= 1
        elif i == 's':
            b = b ** 2
        elif i == 'o':
            res.append(b)
    return res


print(parse('iiisdoso'))
assert parse('iiisdoso') == [8, 64]
